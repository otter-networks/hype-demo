git clone https://github.com/emilyrmeads/hype-demo.git
docker build -t gcr.io/$DEVSHELL_PROJECT_ID/$USER:master .
docker push gcr.io/$DEVSHELL_PROJECT_ID/$USER:master
kubectl create namespace $USER
cat k8s/deployment.yaml | envsubst | kubectl apply -f -
kubectl apply -f k8s/service.yaml
cat k8s/ingress.yaml | envsubst | kubectl apply -f -
