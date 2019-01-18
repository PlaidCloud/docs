# Kubernetes Configuration
All of the files within this directory (and subdirectories) are yaml definitions for everything in our kubernetes environment. The goal is to keep them organized by application, with anything directly responsible for provisioning a plaidcloud container in the root directory.

There are 

`kubectl apply -f deployment.yaml`


## Files (In the order they should be run)

* `deployment.yaml`
  * Defines a kubernetes deployment with a pod template.

## Directories

* `ingress`
  * The configuration files within this directory are for setting up everything necessary for allowing external connections to our cluster, i.e. an ingress controller. This is how we map DNS routes to our apps (plaid, plaid-client, git-service, etc).
* `helm-configs`
  * These are the values.yaml files used for configuring charts. They follow the convention of `<chart-name>-values.yaml`, with the exception of `tiller.yaml`.