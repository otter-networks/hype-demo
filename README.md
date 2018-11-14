## Basic application on Kubernetes
This excercise will get you up and running with a basic application on the Google Cloud Platform (GCP) Google Kubernetes Engine (GKE). In the excercise you will build a docker container and deploy it into GKE using some templated YAML.

Once you have a working Google Cloud account attached to a Project; open the following URL [https://console.cloud.google.com/home/dashboard?project=hype-de-workshop](https://console.cloud.google.com/home/dashboard?project=hype-de-workshop)

In the top right hand corner you should see a button that looks like `>_`. Click it and a terminal will open in the browser.

git clone https://github.com/emilyrmeads/hype-demo.git

docker build -t gcr.io/$DEVSHELL_PROJECT_ID/$USER:master .
docker push gcr.io/$DEVSHELL_PROJECT_ID/$USER:master
gcloud container clusters get-credentials standard-cluster-1 --zone europe-west1-c --project hype-de-workshop
kubectl create namespace $USER
cat k8s/deployment.yaml | envsubst | kubectl apply -f -
kubectl apply -f k8s/service.yaml
cat k8s/ingress.yaml | envsubst | kubectl apply -f -
