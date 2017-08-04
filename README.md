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

O endpoint para obter o número de imóveis por cidade é [http://localhost/api/v1/realties_by_cities](http://localhost/api/v1/realties_by_cities)

### Para executar remotamente

A aplicação está disponível em [neste link](http://165.227.69.119/).

O endpoint para obter o número de imóveis por cidade é [http://165.227.69.119/api/v1/realties_by_cities](http://165.227.69.119/api/v1/realties_by_cities)
