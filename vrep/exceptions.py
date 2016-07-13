from vrepConst import *


class Error(RuntimeError):
    """ Base class for exceptions in this module """

    def __init__(self, message):
        super(Error, self).__init__(message)


class RemoteApiError(Error):
    """ Indicates that a remote api call has failed (non-zero return code) """

    def __init__(self, return_code):
        self.return_code = return_code
        super(RemoteApiError, self).__init__(self._as_string())

    def _as_string(self):
        errors = str(self.return_code) + " :"
        if self.return_code & simx_return_novalue_flag:
            errors += " novalue"
        if self.return_code & simx_return_timeout_flag:
            errors += " timeout"
        if self.return_code & simx_return_illegal_opmode_flag:
            errors += " illegal_opmode"
        if self.return_code & simx_return_remote_error_flag:
            errors += " remote_error"
        if self.return_code & simx_return_split_progress_flag:
            errors += " split_progress"
        if self.return_code & simx_return_local_error_flag:
            errors += " local_error"
        if self.return_code & simx_return_initialize_error_flag:
            errors += " initialize_error"
        return errors


def check_return_ok(ret):
    if ret != vrep.simx_return_ok:
        raise RemoteApiError(ret)
