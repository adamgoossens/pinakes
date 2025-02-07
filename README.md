<img src="./docs/logo-masthead.svg"/>

[![Python package](https://github.com/ansible/pinakes/actions/workflows/python-package.yml/badge.svg)](https://github.com/ansible/pinakes/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/ansible/pinakes/branch/devel/graph/badge.svg?token=GmTfoOt6WW)](https://codecov.io/gh/ansible/pinakes)

Pinakes is the upstream community project for RedHat's [Automation Services Catalog product.](https://www.ansible.com/products/automation-services-catalog?hsLang=en-us)

Pinakes allows customers to expose their Ansible Job Templates and Workflows to business users with an added layer of governance. The Job Templates and Workflows are wrapped as Products into Portfolios which can be shared with different business users. An approval workflow can be attached to Products or Portfolios which adds governance and, in the future, will be able to notify the appropriate Administrators via email. Upon approval, the Job Template or workflow will be launched on the Automation Controller.

Pinakes in the future will also support editing of Survey Specs to create different flavors of the Job Template or Workflow with pre-canned parameters so businesss users don't have to be concerned about the details of a parameter.

For more information about our architecture and services we depend on, see the [architecture doc](./docs/ARCHITECTURE.md)

Installation
------------

If you would like to install Pinakes primarily as a user without needing or wanting to make code changes, please view the [installation guide with minikube environment](./docs/MINIKUBE.md). This should be the default use-case for most users.

Also available are [docker environment](./docs/DOCKER_COMPOSE.md) or [vagrant environment](./docs/VAGRANT.md) instructions, but we heavily encourage and recommend the use of minikube.

If you would like to install Pinakes with the intention of contributing to the codebase, please see below.

If you would like to install Pinakes in a production or production-like environment, please be aware that we do not officially support production environments with Pinakes. However, if you would like to install Pinakes in this manner, please view this [installation guide](./INSTALL.md)

Contributing
------------

- Refer to the [Contribution guide](./docs/CONTRIBUTING.md)
- All code submissions are made through pull requests against the `devel` branch
- Take care to make sure no merge commits are in the submission, and use `git rebase` vs `git merge` for this reason.


Reporting Issues
----------------

If you're experiencing a problem that you feel is a bug in Pinakes or have ideas for improving Pinakes, we encourage you to open an issue and share your feedback.


Code of Conduct
---------------

We ask all of our community members and contributors to adhere to the [Ansible code of conduct](http://docs.ansible.com/ansible/latest/community/code_of_conduct.html). If you have questions or need assistance, please reach out to our community team at [codeofconduct@ansible.com](mailto:codeofconduct@ansible.com) But before opening a new issue, we ask that you please take a look at our [Issues guide](./ISSUES.md).)


Meaning/Pronounciation
----------------------

Pinakes is a bibliographic work widely considered to be the first library catalog, with its contents being based upon the holdings of the Library of Alexandria.

Pinakes is pronounced: /ˈpi.na.kes/
