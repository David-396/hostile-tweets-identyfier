docker build -t david4554545/hostile-tweets-identifier:1.0 .
docker run  --name hostile_tweets_identifier -p 8080:8080 -d david4554545/hostile-tweets-identifier:1.0


oc apply -f ..\infra\hostile-tweets-secret.yaml
oc apply -f ..\infra\app-deployment.yaml
oc apply -f ..\infra\app-svc.yaml
oc apply -f ..\infra\hostile-tweets-secret.yaml