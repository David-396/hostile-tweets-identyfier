cd ..
docker rmi david4554545/hostile-tweets-identifier:latest
docker build -t david4554545/hostile-tweets-identifier:latest .
docker run  --name hostile_tweets_identifier -p 8080:8080 -d david4554545/hostile-tweets-identifier:1.0
docker push david4554545/hostile-tweets-identifier:latest

oc delete deployment hostile-tweets-identifier
oc delete secret hostile-tweets-secret
oc delete svc hostile-tweets-svc
oc delete route hostile-tweets-app-route

 cd .\scripts
oc apply -f ..\infra\hostile-tweets-secret.yaml
oc apply -f ..\infra\app-deployment.yaml
oc apply -f ..\infra\app-svc.yaml
oc apply -f ..\infra\app-route.yaml