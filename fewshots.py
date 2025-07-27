# fewshots.py

analyser_fs = [
    {
        "prompt": "Deploy 50 IoT sensors and connect them to available edge nodes.",
        "output": {
            "deployment_goals": {
                "total_iot_devices": 50,
                "connect_to_edge": True,
                "minimize_latency": False
            },
            "constraints": {
                "max_power": None,
                "use_all_edge_nodes": False
            },
            "preferences": {
                "balanced_distribution": True,
                "avoid_overload": True
            }
        }
    },
    {
        "prompt": "I want to deploy 80 sensors but limit total power usage. Try to balance the load across edge nodes.",
        "output": {
            "deployment_goals": {
                "total_iot_devices": 80,
                "connect_to_edge": True,
                "minimize_latency": False
            },
            "constraints": {
                "max_power": "low",
                "use_all_edge_nodes": False
            },
            "preferences": {
                "balanced_distribution": True,
                "avoid_overload": True
            }
        }
    },
    {
        "prompt": "Place 100 sensors in the system. Make sure the latency is as low as possible.",
        "output": {
            "deployment_goals": {
                "total_iot_devices": 100,
                "connect_to_edge": True,
                "minimize_latency": True
            },
            "constraints": {
                "max_power": None,
                "use_all_edge_nodes": False
            },
            "preferences": {
                "balanced_distribution": False,
                "avoid_overload": True
            }
        }
    },
    {
        "prompt": "Distribute 60 devices evenly using all edge nodes.",
        "output": {
            "deployment_goals": {
                "total_iot_devices": 60,
                "connect_to_edge": True,
                "minimize_latency": False
            },
            "constraints": {
                "max_power": None,
                "use_all_edge_nodes": True
            },
            "preferences": {
                "balanced_distribution": True,
                "avoid_overload": True
            }
        }
    }
]
planner_fs = [
    { 
        "intent": {
            "deployment_goals": {
                "total_iot_devices": 50,
                "connect_to_edge": True,
                "minimize_latency": False
            },
            "constraints": {
                "max_power": None,
                "use_all_edge_nodes": False
            },
            "preferences": {
                "balanced_distribution": True,
                "avoid_overload": True
            }
        },
        "specs":{
            "IoT_Sensors": { 
                "type": "IoT",
                "cpu": 0.2,
                "ram": 0.1,
                "bandwidth_to_edge": 0.5,  # Mbps
                "power": 1.5,
                "count": 50, 
                "connected_to": None,
                "latency": {"Edge_Nodes_A": 5, "Cloud_Node_1": 50, "IoT_Sensors_A": 0}

            },
            "Edge_Nodes": { 
                "type": "Edge",
                "cpu_capacity": 8,           # Total CPUs
                "ram_capacity": 16,          # GB
                "bandwidth_capacity": 20,    # Mbps total incoming from IoT
                "bandwidth_to_cloud": 5,  # Mbps  
                "connected_iot": [],
                "latency": {"Edge_Node_A": 0, "Cloud_Node_1": 50, "IoT_Sensor_A": 5},
                "count": 2 
            },
            "Cloud_Node": {
                "type": "Cloud",
                "cpu_capacity": 32,
                "ram_capacity": 128,
                "bandwidth_capacity": 100,
                "latency": {"Edge_Nodes_A": 50, "Cloud_Node_1": 0, "IoT_Sensors_A": 50} ,
                "connected_edge": []
            }
        },
        "last_plan": {},
        "output":{
                "Chain of Thought": "To deploy 50 IoT sensors, we will connect them to the available edge nodes. Each IoT sensor requires 0.2 CPU and 0.1 GB RAM, with a bandwidth of 0.5 Mbps to the edge. The edge nodes have a total CPU capacity of 8 (0.2 * 40) and RAM capacity of 16 GB (0.1 * 160), with a bandwidth capacity of 20 Mbps (0.5 * 40)for incoming IoT data. So the max amount of iot devices that can be connected to an edge in 40 (smallest constraint). We will need 1 more edge node to be able to use all 50 devices. According to the intent we need to distribute the sensors evenly across the two edge nodes to balance the load and ensure efficient resource usage.",
                "plan": {"IoT_Sensors_A": { 
                    "type": "IoT",
                    "cpu": 0.2,
                    "ram": 0.1,
                    "bandwidth_to_edge": 0.5,
                    "power": 1.5,
                    "count": 25, 
                    "connected_to": "Edge_Nodes_A",
                    "latency": {"Edge_Nodes_A": 5, "Cloud_Node_1": 50, "IoT_Sensors_A": 0}
                },
                "IoT_Sensors_B": { 
                    "type": "IoT",
                    "cpu": 0.2,
                    "ram": 0.1,
                    "bandwidth_to_edge": 0.5,
                    "power": 1.5,
                    "count": 25, 
                    "connected_to": "Edge_Nodes_B",
                    "latency": {"Edge_Nodes_A": 5, "Edge_Nodes_B": 5, "Cloud_Node_1": 50, "IoT_Sensors_A": 0}

                }, 
                "Edge_Node_A": { 
                    "type": "Edge",
                    "cpu_capacity": 8,
                    "ram_capacity": 16, 
                    "bandwidth_capacity": 20,
                    "bandwidth_to_cloud": 5, 
                    "connected_iot": ["IoT_Sensors_A"],
                    "latency": {"Edge_Node_A": 0, "Edge_Node_B": 5,"Cloud_Node_1": 50, "IoT_Sensor_A": 5, "IoT_Sensor_B": 5},
                },
                "Edge_Node_B": { 
                    "type": "Edge",
                    "cpu_capacity": 8,
                    "ram_capacity": 16,
                    "bandwidth_capacity": 20,
                    "bandwidth_to_cloud": 5,
                    "connected_iot": ["IoT_Sensors_B"],
                    "latency": {"Edge_Node_A": 5, "Edge_Node_B": 0, "Cloud_Node_1": 50, "IoT_Sensor_A": 5, "IoT_Sensor_B": 5},
                }, 
                "Cloud_Node": {
                    "type": "Cloud",
                    "cpu_capacity": 32,
                    "ram_capacity": 128,
                    "bandwidth_capacity": 100,
                    "latency": {"Edge_Nodes_A": 50, "Cloud_Node_1": 0, "IoT_Sensors_A": 50} ,
                    "connected_edge": ["Edge_Nodes_A", "Edge_Nodes_B"]
                }
}} 
    },
    {
  "intent": {
    "deployment_goals": {
      "total_iot_devices": 80,
      "connect_to_edge": True,
      "minimize_latency": True
    },
    "constraints": {
      "max_power": None,
      "use_all_edge_nodes": False
    },
    "preferences": {
      "balanced_distribution": False,
      "avoid_overload": True
    }
  },
  "specs": {
    "IoT_Sensors": {
      "type": "IoT",
      "cpu": 0.1,
      "ram": 0.05,
      "bandwidth_to_edge": 0.2,
      "power": 1.0,
      "count": 80,
      "connected_to": None,
      "latency": {"Edge_A": 2, "Edge_B": 4}
    },
    "Edge_A": {
      "type": "Edge",
      "cpu_capacity": 10,
      "ram_capacity": 8,
      "bandwidth_capacity": 10,
      "bandwidth_to_cloud": 5,
      "connected_iot": [],
      "latency": {"Cloud": 40},
      "count": 1
    },
    "Edge_B": {
      "type": "Edge",
      "cpu_capacity": 10,
      "ram_capacity": 8,
      "bandwidth_capacity": 10,
      "bandwidth_to_cloud": 5,
      "connected_iot": [],
      "latency": {"Cloud": 50},
      "count": 1
    },
    "Cloud": {
      "type": "Cloud",
      "cpu_capacity": 64,
      "ram_capacity": 256,
      "bandwidth_capacity": 200,
      "latency": {"Edge_A": 40, "Edge_B": 50}
    }
  },
  "last_plan": {},
  "output": {
    "Chain of Thought": "The goal is to minimize latency. Edge_A has lower latency (2ms vs 4ms) and can support up to 50 IoT devices based on bandwidth (0.2 * 50 = 10) and CPU (0.1 * 50 = 5 CPU; 0.05 * 50 = 2.5 GB RAM; 0.2 * 50 = 10 Mbps). Edge_B has identical capacity, so we we can place maximum 50 on each. Since balanced distribution is not required, we prioritize Edge_A first to meet the low-latency goal with 50 and 30 on Edge_B.",
    "plan": {
      "IoT_Sensors_A": {
        "type": "IoT",
        "cpu": 0.1,
        "ram": 0.05,
        "bandwidth_to_edge": 0.2,
        "power": 1.0,
        "count": 50,
        "connected_to": "Edge_A",
        "latency": {"Edge_A": 2, "Edge_B": 4}
      },
      "IoT_Sensors_B": {
        "type": "IoT",
        "cpu": 0.1,
        "ram": 0.05,
        "bandwidth_to_edge": 0.2,
        "power": 1.0,
        "count": 30,
        "connected_to": "Edge_B",
        "latency": {"Edge_A": 2, "Edge_B": 4}
      },
      "Edge_A": {
        "type": "Edge",
        "cpu_capacity": 10,
        "ram_capacity": 8,
        "bandwidth_capacity": 10,
        "bandwidth_to_cloud": 5,
        "connected_iot": ["IoT_Sensors_A"],
        "latency": {"Cloud": 40}
      },
      "Edge_B": {
        "type": "Edge",
        "cpu_capacity": 10,
        "ram_capacity": 8,
        "bandwidth_capacity": 10,
        "bandwidth_to_cloud": 5,
        "connected_iot": ["IoT_Sensors_B"],
        "latency": {"Cloud": 50}
      },
      "Cloud": {
        "type": "Cloud",
        "cpu_capacity": 64,
        "ram_capacity": 256,
        "bandwidth_capacity": 200,
        "latency": {"Edge_A": 40, "Edge_B": 50}
      }
    }
  }
},
{
  "intent": {
    "deployment_goals": {
      "total_iot_devices": 60,
      "connect_to_edge": True,
      "minimize_latency": False
    },
    "constraints": {
      "max_power": None,
      "use_all_edge_nodes": True
    },
    "preferences": {
      "balanced_distribution": True,
      "avoid_overload": True
    }
  },
  "specs": {
    "IoT_Sensors": {
      "type": "IoT",
      "cpu": 0.2,
      "ram": 0.1,
      "bandwidth_to_edge": 0.5,
      "power": 2.0,
      "count": 60,
      "connected_to": None,
      "latency": {"Edge_1": 10, "Edge_2": 10}
    },
    "Edge_1": {
      "type": "Edge",
      "cpu_capacity": 8,
      "ram_capacity": 8,
      "bandwidth_capacity": 20,
      "bandwidth_to_cloud": 5,
      "connected_iot": [],
      "latency": {"Cloud": 40},
      "count": 1
    },
    "Edge_2": {
      "type": "Edge",
      "cpu_capacity": 8,
      "ram_capacity": 8,
      "bandwidth_capacity": 20,
      "bandwidth_to_cloud": 5,
      "connected_iot": [],
      "latency": {"Cloud": 40},
      "count": 1
    },
    "Cloud": {
      "type": "Cloud",
      "cpu_capacity": 64,
      "ram_capacity": 256,
      "bandwidth_capacity": 200,
      "latency": {"Edge_1": 40, "Edge_2": 40}
    }
  },
  "last_plan": {},
  "output": {
    "Chain of Thought": "Each IoT device needs 0.2 CPU, 0.1 RAM, and 0.5 Mbps. Edge nodes can handle a maximum of 40 sensors each (based on cpu, ram, and bandwidth). There are 60 sensors, since we must use all edge nodes and distribute evenly, we split 30 sensors to each.",
    "plan": {
    "IoT_Sensors_1": {
        "type": "IoT",
        "cpu": 0.2,
        "ram": 0.1,
        "bandwidth_to_edge": 0.5,
        "power": 2.0,
        "count": 30,
        "connected_to": "Edge_1",
        "latency": {"Edge_1": 10, "Edge_2": 10}
      },
    "IoT_Sensors_2": {
        "type": "IoT",
        "cpu": 0.2,
        "ram": 0.1,
        "bandwidth_to_edge": 0.5,
        "power": 2.0,
        "count": 30,
        "connected_to": "Edge_2",
        "latency": {"Edge_1": 10, "Edge_2": 10}
      },
    "Edge_1": {
      "type": "Edge",
      "cpu_capacity": 8,
      "ram_capacity": 8,
      "bandwidth_capacity": 20,
      "bandwidth_to_cloud": 5,
      "connected_iot": ["IoT_Sensors_1"],
      "latency": {"Cloud": 40},
      "count": 1
    },
    "Edge_2": {
      "type": "Edge",
      "cpu_capacity": 8,
      "ram_capacity": 8,
      "bandwidth_capacity": 20,
      "bandwidth_to_cloud": 5,
      "connected_iot": ["IoT_Sensors_2"],
      "latency": {"Cloud": 40},
      "count": 1
    },
    "Cloud": {
      "type": "Cloud",
      "cpu_capacity": 64,
      "ram_capacity": 256,
      "bandwidth_capacity": 200,
      "latency": {"Edge_1": 40, "Edge_2": 40}
    }
    }
  }
},
{
  "intent": {
    "deployment_goals": {
      "total_iot_devices": 90,
      "connect_to_edge": True,
      "minimize_latency": False
    },
    "constraints": {
      "max_power": None,
      "use_all_edge_nodes": False,
    },
    "preferences": {
      "balanced_distribution": True,
      "avoid_overload": True,
        "allow_direct_cloud": True
    }
  },
  "specs": {
    "IoT_Sensors": {
      "type": "IoT",
      "cpu": 0.2,
      "ram": 0.1,
      "bandwidth_to_edge": 0.5,
      "power": 2.0,
      "count": 90,
      "connected_to": None,
      "latency": {"Edge_A": 6, "Cloud": 50}
    },
    "Edge_A": {
      "type": "Edge",
      "cpu_capacity": 10,
      "ram_capacity": 5,
      "bandwidth_capacity": 15,
      "bandwidth_to_cloud": 2,
      "connected_iot": [],
      "latency": {"Cloud": 40}
    },
    "Cloud": {
      "type": "Cloud",
      "cpu_capacity": 128,
      "ram_capacity": 512,
      "bandwidth_capacity": 500,
      "latency": {"Edge_A": 40}
    }
  },
  "last_plan": {},
  "output": {
    "Chain of Thought": "Edge_A can only host up to 30 devices (0.2*30 = 6 CPU, 0.1*30 = 3 RAM, 0.5*30 = 15 Mbps). Since we need to place 90 sensors, the remaining 60 will be routed directly to the cloud because allow_direct_cloud is True. This keeps Edge_A from overloading while achieving the goal of placing all devices.",
    "plan": {
      "IoT_Sensors_Edge": {
        "type": "IoT",
        "cpu": 0.2,
        "ram": 0.1,
        "bandwidth_to_edge": 0.5,
        "power": 2.0,
        "count": 30,
        "connected_to": "Edge_A",
        "latency": {"Edge_A": 6, "Cloud": 50}
      },
      "IoT_Sensors_Cloud": {
        "type": "IoT",
        "cpu": 0.2,
        "ram": 0.1,
        "bandwidth_to_edge": 0.5,
        "power": 2.0,
        "count": 60,
        "connected_to": "Cloud",
        "latency": {"Edge_A": 6}
      },
    "Edge_A": {
      "type": "Edge",
      "cpu_capacity": 10,
      "ram_capacity": 5,
      "bandwidth_capacity": 15,
      "bandwidth_to_cloud": 2,
      "connected_iot": ["IoT_Sensors_Edge"],
      "latency": {"Cloud": 40}
    },
    "Cloud": {
      "type": "Cloud",
      "cpu_capacity": 128,
      "ram_capacity": 512,
      "bandwidth_capacity": 500,
      "latency": {"Edge_A": 40, "IoT_Sensors_Cloud": 50},
      "connected_edge": ["Edge_A", "IoT_Sensors_Cloud"]
    }

    }
  }
},
{
  "intent": {
    "deployment_goals": {
      "total_iot_devices": 75,
      "connect_to_edge": True,
      "minimize_latency": True
    },
    "constraints": {
      "max_power": None,
      "use_all_edge_nodes": True
    },
    "preferences": {
      "balanced_distribution": False,
      "avoid_overload": True
    }
  },
  "specs": {
    "IoT_Sensor_Type_A": {
      "type": "IoT",
      "cpu": 0.1,
      "ram": 0.1,
      "bandwidth_to_edge": 0.3,
      "power": 1.2,
      "count": 25,
      "connected_to": None,
      "latency": {"Edge_A": 5, "Edge_B": 15, "Cloud": 80}
    },
    "IoT_Sensor_Type_B": {
      "type": "IoT",
      "cpu": 0.2,
      "ram": 0.2,
      "bandwidth_to_edge": 0.5,
      "power": 1.8,
      "count": 25,
      "connected_to": None,
      "latency": {"Edge_A": 4, "Edge_B": 10, "Cloud": 90}
    },
    "IoT_Sensor_Type_C": {
      "type": "IoT",
      "cpu": 0.15,
      "ram": 0.1,
      "bandwidth_to_edge": 0.4,
      "power": 1.4,
      "count": 25,
      "connected_to": None,
      "latency": {"Edge_A": 20, "Edge_B": 5, "Cloud": 70}
    },
    "Edge_A": {
      "type": "Edge",
      "cpu_capacity": 16,
      "ram_capacity": 32,
      "bandwidth_capacity": 40,
      "bandwidth_to_cloud": 10,
      "connected_iot": [],
      "latency": {"Edge_A": 0, "Edge_B": 10, "Cloud": 50}
    },
    "Edge_B": {
      "type": "Edge",
      "cpu_capacity": 16,
      "ram_capacity": 32,
      "bandwidth_capacity": 40,
      "bandwidth_to_cloud": 10,
      "connected_iot": [],
      "latency": {"Edge_A": 10, "Edge_B": 0, "Cloud": 50}
    },
    "Cloud": {
      "type": "Cloud",
      "cpu_capacity": 64,
      "ram_capacity": 256,
      "bandwidth_capacity": 200,
      "latency": {"Edge_A": 50, "Edge_B": 50}
    }
  },
  "last_plan": {},
  "output": {
    "Chain of Thought": "The user wants to deploy 75 IoT devices with minimized latency and full edge node utilization. Sensor A and B have much lower latency to Edge_A, and Sensor C has lowest latency to Edge_B. To meet the minimize-latency and avoid-overload goals, Sensor_A and Sensor_B will be connected to Edge_A, while Sensor_C will be connected to Edge_B. Resource capacities on both edges are sufficient to handle their assigned loads.",
    "plan": {
      "IoT_Sensor_Type_A": {
        "type": "IoT",
        "cpu": 0.1,
        "ram": 0.1,
        "bandwidth_to_edge": 0.3,
        "power": 1.2,
        "count": 25,
        "connected_to": "Edge_A",
        "latency": {"Edge_A": 5, "Edge_B": 15, "Cloud": 80}
      },
      "IoT_Sensor_Type_B": {
        "type": "IoT",
        "cpu": 0.2,
        "ram": 0.2,
        "bandwidth_to_edge": 0.5,
        "power": 1.8,
        "count": 25,
        "connected_to": "Edge_A",
        "latency": {"Edge_A": 4, "Edge_B": 10, "Cloud": 90}
      },
      "IoT_Sensor_Type_C": {
        "type": "IoT",
        "cpu": 0.15,
        "ram": 0.1,
        "bandwidth_to_edge": 0.4,
        "power": 1.4,
        "count": 25,
        "connected_to": "Edge_B",
        "latency": {"Edge_A": 20, "Edge_B": 5, "Cloud": 70}
      },
      "Edge_A": {
        "type": "Edge",
        "cpu_capacity": 16,
        "ram_capacity": 32,
        "bandwidth_capacity": 40,
        "bandwidth_to_cloud": 10,
        "connected_iot": ["IoT_Sensor_Type_A", "IoT_Sensor_Type_B"],
        "latency": {"Edge_A": 0, "Edge_B": 10, "Cloud": 50}
      },
      "Edge_B": {
        "type": "Edge",
        "cpu_capacity": 16,
        "ram_capacity": 32,
        "bandwidth_capacity": 40,
        "bandwidth_to_cloud": 10,
        "connected_iot": ["IoT_Sensor_Type_C"],
        "latency": {"Edge_A": 10, "Edge_B": 0, "Cloud": 50}
      },
      "Cloud": {
        "type": "Cloud",
        "cpu_capacity": 64,
        "ram_capacity": 256,
        "bandwidth_capacity": 200,
        "latency": {"Edge_A": 50, "Edge_B": 50}
      }
    }
  }
}




    ]
optimizer_fs = []
 