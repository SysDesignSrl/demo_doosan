## OPC-UA
### Structures
```

```
### Methods
---
### move_home
> Homing is performed by moving to the joint motion to the mechanical or user defined home position.
> According to the input parameter [target], it moves to the mechanical home defined in the system or the home set by the user.

#### Request
| Type       | Name      | Value                      | Description
|------------|-----------|:--------------------------:|----------------------------------
| int8       | target    | DR_HOME_TARGET_MECHANIC(0) | Mechanical home, joint angle (0,0,0,0,0,0)
|            |           | DR_HOME_TARGET_USER(1)     | User home

#### Response
| Type       | Name      | Value                      | Description
|------------|-----------|----------------------------|----------------------------------
| int8       | res       |                            | 0=success, otherwise fail
| bool       | success   |                            |

---
### move joint
> The robot moves to the target joint position (pos) from the current joint position.

#### Request
| Type       | Name      | Value                      | Description
|------------|-----------|:--------------------------:|---------------------------
| float64[6] | pos       |                            | target joint angle list [degree]
| float64    | vel       |                            | set velocity: [deg/sec]
| float64    | acc       |                            | set acceleration: [deg/sec2]
| float64    | time      | 0.0                        | Time [sec]
| float64    | radius    | 0.0                        | Radius under blending mode [mm]
| int8       | mode      | MOVE_MODE_ABSOLUTE=0       |
|            |           | MOVE_MODE_RELATIVE=1       |
| int8       | blendType | BLENDING_SPEED_TYPE_DUPLICATE=0 |
|            |           | BLENDING_SPEED_TYPE_OVERRIDE=1  |
| int8       | syncType  | SYNC = 0                        |
|            |           | ASYNC = 1                       |

#### Response
| Type       | Name      | Value | Description
|------------|-----------|:-----:|-----------------------------------------------
| bool       | success   |       |

---
### move line
>

#### Request
| Type       | Name      | Value | Description
|------------|-----------|:-----:|------------------------------------------------
| float64[6] | pos       |       | target  
| float64[2] | vel       |       | set velocity: [mm/sec], [deg/sec]
| float64[2] | acc       |       | set acceleration: [mm/sec2], [deg/sec2]
| float64    | time      | 0.0   | Time [sec]
| float64    | radius    | 0.0   | Radius under blending mode [mm]
| int8       | ref       |       | DR_BASE(0), DR_TOOL(1), DR_WORLD(2)
| int8       | mode      | 0     | DR_MV_MOD_ABS(0), DR_MV_MOD_REL(1)
| int8       | blendType | 0     | BLENDING_SPEED_TYPE_DUPLICATE=0, BLENDING_SPEED_TYPE_OVERRIDE=1
| int8       | syncType  | 0     | SYNC = 0, ASYNC = 1

#### Response
| Type       | Name      | Value | Description
|------------|-----------|:-----:|--------------------------------------------------
| bool       | success   |       |

---
### move circle
>

#### Request
| Type         | Name        | Value | Description
|--------------|-------------|:-----:|------------------------------------------
std_msgs/Float64MultiArray[] | pos | | target[2][6]  
float64[2]     | vel         |       | set velocity: [mm/sec], [deg/sec]
float64[2]     | acc         |       | set acceleration: [mm/sec2], [deg/sec2]
float64        | time        | 0.0   | Time [sec]
float64        | radius      | 0.0   | Radius under blending mode [mm]
int8           | ref         |       | DR_BASE(0), DR_TOOL(1), DR_WORLD(2)
int8           | mode        | 0     | MOVE_MODE_ABSOLUTE=0, MOVE_MODE_RELATIVE=1
float64        | angle1      | 0.0   | angle1 [degree]
float64        | angle2      | 0.0   | angle2 [degree]
int8           | blendType   | 0     | BLENDING_SPEED_TYPE_DUPLICATE=0, BLENDING_SPEED_TYPE_OVERRIDE=1
int8           | syncType    | 0     | SYNC = 0, ASYNC = 1

#### Response
| Type         | Name        | Value | Description
|--------------|-------------|:-----:|------------------------------------------
| bool         | success     |       |

---
### move blending
>

#### Request
| Type         | Name          | Value       | Description
|--------------|---------------|:-----------:|----------------------------------
| std_msgs/Float64MultiArray[] | segment     | | 50 x (pos1[6]:pos2[6]:type[1]:radius[1])        
| int8         | posCnt        |             | target cnt
| float64[2]   | vel           |             | set velocity: [mm/sec], [deg/sec]
| float64[2]   | acc           |             | set acceleration: [mm/sec2], [deg/sec2]
| float64      | time          | 0.0         | Time [sec]
| int8         | ref           | DR_BASE(0)  |
|              |               | DR_TOOL(1)  |
|              |               | DR_WORLD(2) |
| int8         | mode          | 0           | MOVE_MODE_ABSOLUTE=0, MOVE_MODE_RELATIVE=1
| int8         | syncType      | 0           | SYNC = 0, ASYNC = 1

#### Response
| Type     | Name              | Value       | Description
|----------|-------------------|:-----------:|----------------------------------
| bool     | success           |             |

---
### motion pause
>
#### Request
| Type       | Name            | Value       | Description
|------------|-----------------|-------------|----------------------------------

#### Response
| Type       | Name            | Value       | Description
|------------|-----------------|-------------|----------------------------------
| bool       | success         |             |

---
### motion resume
>

#### Request
| Type       | Name            | Value       | Description
|------------|-----------------|-------------|----------------------------------

#### Response
| Type       | Name            | Value       | Description
|------------|-----------------|-------------|----------------------------------
| bool       | success         |             |

---
#### stop
>

#### Request
| Type       | Name      | Value           | Description
|------------|-----------|:---------------:|------------------------------------
| int32      | stop_mode | DR_QSTOP_STO(0) | Quick stop (Stop Category 1 without STO(Safe Torque Off)
|            |           | DR_QSTOP(1)     | Quick stop (Stop Category 2)
|            |           | DR_SSTO(2)      | Soft Stop
|            |           | DR_HOLD(3)      | HOLD stop

#### Response
| Type       | Name      | Value           | Description
|------------|-----------|:---------------:|------------------------------------
| bool       | success   |                 |

---
