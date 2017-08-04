# Exame Ads

### Para executar localmente

É necessário executar os contêineres, criar as imagens, iniciar os serviços e criar as tabelas no banco de dados 
(PostgreSQL).

```
docker-compose build
docker-compose up -d
docker-compose run web /usr/local/bin/python create_db.py
```

É preciso importar os dados dos arquivos .csv localizados na pasta db_dump para as suas respectivas tabelas.

A aplicação estará disponível em [http://localhost/](http://localhost/).

### Para executar remotamente

A aplicação está disponível em [neste link](http://165.227.69.119/).