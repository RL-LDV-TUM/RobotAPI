from exceptions import *
import synchronous as api


class Object(object):
    def __init__(self, clientID, name=None, handle=None):
        self._clientID = clientID
        if handle is not None:
            self._handle = handle
            self._name = api.get_object_name(clientID, handle)
            return
        if name is not None:
            self._name = name
            self._handle = api.get_object_handle(clientID, name)
            return
        raise Error(
            "Neither handle nor name defined, cannot construct object")

    def __repr__(self):
        return "vrep Object: {}".format(self._name)

    def __iter__(self):
        """
        Iterate over the children objects
        """
        i = 0
        while(True):  # I assume there can be a max of 1024, no idea though
            childHandle = api.get_object_child_handle(clientID=self._clientID,
                                                      objectHandle=self._handle,
                                                      childIndex=i)
            i = i + 1
            if childHandle == -1:
                raise StopIteration()
            else:
                yield Object(clientID=self._clientID, handle=childHandle)

    def name(self):
        return self._name

    def position(self, relativeTo=None):
        """ Retrieve the position of this object as vector of floats [x y z] """
        other_handle = -1  # means absolute position
        if relativeTo is not None:
            other_handle = Object(clientID=self._clientID,
                                  name=relativeTo)._handle
        return api.get_object_position(clientID=self._clientID,
                                       objectHandle=self._handle,
                                       otherObjectHandle=other_handle)

    def set_position(self, newPosition, relativeTo=None):
        """ Set the position of this object as vector of floats [x y z] """
        other_handle = -1  # means absolute position
        if relativeTo is not None:
            other_handle = Object(clientID=self._clientID,
                                  name=relativeTo)._handle
        api.set_object_position(clientID=self._clientID,
                                objectHandle=self._handle,
                                otherObjectHandle=other_handle,
                                position=newPosition)

    def orientation(self, relativeTo=None):
        """ Retrieve the orientation of this object as vector of float angles [a b c]"""
        other_handle = -1  # absolute orientation in scene
        if relativeTo is not None:
            other_handle = Object(clientID=self._clientID,
                                  name=relativeTo)._handle
        return api.get_object_orientation(clientID=self._clientID,
                                          objectHandle=self._handle,
                                          otherObjectHandle=other_handle)

    def set_orientation(self, newOrientation, relativeTo=None):
        """ Set the orientation of this object as vector of float angles [a b c]"""
        other_handle = -1  # absolute orientation in scene
        if relativeTo is not None:
            other_handle = Object(clientID=self._clientID,
                                  name=relativeTo)._handle
        api.set_object_orientation(clientID=self._clientID,
                                   objectHandle=self._handle,
                                   otherObjectHandle=other_handle,
                                   orientation=newOrientation)

    def velocity(self):
        """ Retrieve the velocity of this object as vector of float speed [x y z] """
        return api.get_object_velocity(clientID=self._clientID,
                                       objectHandle=self._handle)

    def parent(self):
        parent_handle = api.get_object_parent_handle(clientID=self._clientID,
                                                     clientHandle=self._handle)
        return Object(clientID=self._clientID, handle=parent_handle)


class Joint(Object):
    def __init__(self, clientID, name=None, handle=None):
        super(self.__class__, self).__init__(
            clientID=clientID, name=name, handle=handle)

    def get_state(self):
        """
           Retrieve the position of a joint.
           For rotational joints, this is the angle, in radians [-pi,pi]
           For prismatic joints, this is the translation amount
        """
        return api.get_joint_position(clientID=self._clientID,
                                      objectHandle=self._handle)

    def set_state(self, position):
        api.set_joint_position(clientID=self._clientID,
                               objectHandle=self._handle,
                               newPosition=position)
