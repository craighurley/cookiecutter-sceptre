"""
Provide utility hooks for operating on stacks.

Note: If using var file, ensure you default the parameter otherwise this script will fail, e.g:
    ExampleParameter: '{{ var.ExampleParameter | default("example") }}'
"""

from sceptre.hooks import Hook
from sceptre.environment import Environment

class SetStackTerminationProtection(Hook):
    """
    Enable/disable stack termination protection.
    """

    ALLOWED_ARG_VALUES = ['enabled', 'disabled']

    def __init__(self, *args, **kwargs):
        super(SetStackTerminationProtection, self).__init__(*args, **kwargs)

    def run(self):
        argument = (self.argument if self.argument else '').lower()

        assert argument in self.ALLOWED_ARG_VALUES, \
            "As the argument for !set_stack_termination_protection, please choose one of {0}".format(self.ALLOWED_ARG_VALUES)

        environment = Environment(self.environment_config.sceptre_dir, self.environment_config.environment_path)
        stack = environment.stacks[self.stack_config.name]
        cf_stack_name = stack.external_name

        enable = argument == 'enabled'

        self.logger.info(
            "Setting termination protection of stack '%s' to '%s'",
            cf_stack_name, argument)

        self.connection_manager.call('cloudformation', 'update_termination_protection',
                                    kwargs={
                                        'StackName': cf_stack_name,
                                        'EnableTerminationProtection': enable
                                    })
