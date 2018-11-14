## Basic application on Kubernetes
This excercise will get you up and running with a basic application on the Google Cloud Platform (GCP) Google Kubernetes Engine (GKE). In the excercise you will build a docker container and deploy it into GKE using some templated YAML.

Once you have a working Google Cloud account attached to a Project; open the following URL [https://console.cloud.google.com/home/dashboard?project=hype-de-workshop](https://console.cloud.google.com/home/dashboard?project=hype-de-workshop)

In the top right hand corner you should see a button that looks like `>_`. Click it and a "Cloud Shell" terminal will open in the browser.

#Docker

Clone the repo into the cloud shell environment and go into the directory.
```
git clone https://github.com/otter-networks/hype-demo.git; cd hype-demo
```

We can now build the application into a Docker container. We have used some environment variables to make this easier.
```
docker build -t gcr.io/$DEVSHELL_PROJECT_ID/$USER:master .
```

We can have a look at what images are available on the local system with the `docker images` command.
```
otter@cloudshell:~/hype-demo (hype-de-workshop)$ docker images
REPOSITORY                      TAG                 IMAGE ID            CREATED             SIZE
gcr.io/hype-de-workshop/otter   master              d98307c011de        13 seconds ago      932MB
python                          latest              2cc378c061f7        1 hour ago          923MB
```
This python image is quite large. You can see that the image that we just created added and extra 9MB.

We push the docker container that we just created into into the Google Container Registry (GCR)
```
docker push gcr.io/$DEVSHELL_PROJECT_ID/$USER:master
```
We can see our image in the GCR here: [https://console.cloud.google.com/gcr/images/hype-de-workshop/](https://console.cloud.google.com/gcr/images/hype-de-workshop/)

#Kubernetes 

Now that we have a working docker image we can deploy this application to Kubernetes.

We need to get a 'Kubeconfig'. This chunk of YAML stored in `~/.kube/config` allows us to connect to our Kubernetes Cluster with the `kubectl` tool.
```
gcloud container clusters get-credentials standard-cluster-1 --zone europe-west1-c --project hype-de-workshop
```
 
First, we create a namespace. This is a logical container for all our Kubernetes objects.
```
kubectl create namespace $USER
```

Now we have a namespace we can create a deployment. A deployment describes how many containers (Pods) we want from a particualar image.
```
cat k8s/deployment.yaml | envsubst | kubectl apply -f -
```
A Pod in fact can be more complex than a single container. You can have multiple containers in a Pod which form the smallest deployable unit in Kubernetes. If you have a pod that faciltates connections to databases for instance then this is known as a "Sidecar container"  

A service provides plumbing for our deployment. It provides a single DNS endpoint for all the Pods in a deployment.
```
kubectl apply -f k8s/service.yaml
```

The ingress provides a mapping from a hostname to a service. This allows traffic to enter the cluster an find the appropriate Pods. 
```
cat k8s/ingress.yaml | envsubst | kubectl apply -f -
```
