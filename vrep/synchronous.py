import vrep
from exceptions import *


def get_object_handle(clientID, name):
    ret, handle = vrep.simxGetObjectHandle(
        clientID=clientID,
        objectName=name,
        operationMode=vrep.simx_opmode_oneshot_wait
    )
    check_return_ok(ret)
    return handle


def get_object_parent_handle(clientID, childHandle):
    ret, handle = vrep.simxGetObjectParent(
        clientID=clientID,
        childObjectHandle=childHandle,
        operationMode=vrep.simx_opmode_oneshot_wait
    )
    check_return_ok(ret)
    return handle


def get_object_child_handle(clientID, objectHandle, childIndex):
    ret, childObjectHandle = vrep.simxGetObjectChild(
        clientID=clientID,
        parentObjectHandle=objectHandle,
        childIndex=childIndex,
        operationMode=vrep.simx_opmode_oneshot_wait
    )
    check_return_ok(ret)
    return childObjectHandle


def get_object_name(clientID, objectHandle):
    ret, stringData = vrep.simxGetObjectGroupData(
        clientID=clientID,
        objectType=vrep.simx_appobj_object_type,
        dataType=0,  # object name
        operationMode=vrep.simx_opmode_oneshot_wait
    )
    check_return_ok(ret)
    return stringData[0]


def get_object_position(clientID, objectHandle, otherObjectHandle=-1):
    ret, position = vrep.simxGetObjectPosition(
        clientID=clientID,
        objectHandle=objectHandle,
        relativeToObjectHandle=otherObjectHandle,  # -1 == absolute postion
        operationMode=vrep.simx_opmode_oneshot_wait
    )
    check_return_ok(ret)
    return position


def set_object_position(clientID, objectHandle, position, otherObjectHandle=-1):
    ret = vrep.simxSetObjectPosition(
        clientID=clientID,
        objectHandle=objectHandle,
        relativeToObjectHandle=otherObjectHandle,  # -1 == absolute postion
        position=position,
        operationMode=vrep.simx_opmode_oneshot_wait
    )
    check_return_ok(ret)


def get_object_orientation(clientID, objectHandle, otherObjectHandle=-1):
    ret, orientation = vrep.simxGetObjectOrientation(
        clientID=clientID,
        objectHandle=objectHandle,
        relativeToObjectHandle=otherObjectHandle,  # -1 == relative to scene
        operationMode=vrep.simx_opmode_oneshot_wait
    )
    check_return_ok(ret)
    return orientation


def set_object_orientation(clientID, objectHandle, orientation, otherObjectHandle=-1):
    ret = vrep.simxSetObjectOrientation(
        clientID=clientID,
        objectHandle=objectHandle,
        relativeToObjectHandle=otherObjectHandle,  # -1 == relative to scene
        eulerAngles=orientation,
        operationMode=vrep.simx_opmode_oneshot_wait
    )
    check_return_ok(ret)


def get_object_velocity(clientID, objectHandle):
    ret, linear, angular = vrep.simxGetObjectVelocity(
        clientID=clientID,
        objectHandle=objectHandle,
        operationMode=vrep.simx_opmode_oneshot_wait
    )
    check_return_ok(ret)
    return linear, angular


def get_joint_position(clientID, objectHandle):
    ret, pos = vrep.simxGetJointPosition(
        clientID=clientID,
        jointHandle=objectHandle,
        operationMode=vrep.simx_opmode_oneshot_wait
    )
    check_return_ok(ret)
    return pos


def set_joint_position(clientID, objectHandle, newPosition):
    ret = vrep.simxSetJointPosition(
        clientID=clientID,
        jointHandle=objectHandle,
        position=newPosition,
        operationMode=vrep.simx_opmode_oneshot_wait
    )
    check_return_ok(ret)
