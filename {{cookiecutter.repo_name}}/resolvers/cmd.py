"""
Resolver for running shell commands and returning the value
"""

import subprocess
from sceptre.resolvers import Resolver

class CmdResolver(Resolver):
    """
    Resolver for running shell commands and returning the value
    :param argument: Name of the environment variable to return.
    :type argument: str
    """

    def resolve(self):
        """
        Runs a command and returns the output as a string
        :returns: Value of the environment variable.
        :rtype: str
        """
        op = subprocess.check_output(self.argument, shell=True).decode("utf-8")
        self.logger.debug("CmdResolver returned: '%s'", op)
        return op
