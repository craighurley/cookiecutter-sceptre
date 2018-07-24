# {{ cookiecutter.repo_name }}

{{ cookiecutter.short_description }}

## Setup

1. Install the necessary requirements.

    ```sh
    pip install -r requirements.txt
    ```

1. Update the sceptre environment configuration file, e.g. `dev`:

    ```sh
    vim config/dev/config.yaml
    ```

    Key items to populate are:

    - `environment`: The environment name; already populated correctly.
    - `owner`: The owner of the resources created, useful for billing purposes.
    - `project_code`: A project code, useful to distinguish multiple stacks from each other (e.g. two different users are deploying development stacks at the same time).
    - `region`: The region you are deploying to.
    - `profile`: If you use a AWS profile name to store your access keys, and that profile is not the default profile, use this property to identify the correct profile.

## Deployment

### Stack Deploy

Deploy an environment, e.g. `dev`:

```sh
sceptre --var-file=vars/dev.yaml launch-env dev/network
```

... or deploy a specific stack in an environment:

```sh
sceptre --var-file=vars/dev.yaml launch-stack dev/network vpc
```

### Deletion

Delete the entire environment:

```sh
sceptre --var-file=vars/dev.yaml delete-env dev/netork
```

... or delete a specific stack in an environment:

```sh
sceptre --var-file=vars/dev.yaml delete-stack dev/network vpc
```

## Information

Get information about the deployed environment/stack(s):

```sh
sceptre --var-file=vars/dev.yaml describe-env dev/network
sceptre --var-file=vars/dev.yaml describe-env-resources dev/network
sceptre --var-file=vars/dev.yaml describe-stack-outputs dev/network vpc
```

## Links

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/>
- <https://sceptre.cloudreach.com>
