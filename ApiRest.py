from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import Conection as c
import uvicorn

app = FastAPI()

@app.get('/producao/{year}')
async def ProductionExtract(year: str):
    # Obtenha os parâmetros da URL
    ano = year
    opcao = "opt_02"

    # Crie a conexão com os parâmetros fornecidos
    link = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        "ano": ano,
        "opcao": opcao 
    }

    conection = c.Conection(link, params)
    
    # Extraia a tabela
    table = conection.ExtractTableVitinicultura("ProductionExtract")

    # Retorne os dados em formato JSON
    return JSONResponse(content=table)



@app.get('/processamento/{year}/{subpot}')
async def ProcessingExtract(year: str, subopt_01: str):
    
    # Obtenha os parâmetros da URL
    ano = year
    opcao = "opt_03"

    # Crie a conexão com os parâmetros fornecidos
    link = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        "ano": ano,
        "opcao": opcao,
        "subopcao": subopt_01
    }

    conection = c.Conection(link, params)
    
    # Extraia a tabela
    table = conection.ExtractTableVitinicultura("processamento")

    # Retorne os dados em formato JSON
    return JSONResponse(content=table)



@app.get('/comercializacao/{year}')
async def MarketingExtract(year: str):
    # Obtenha os parâmetros da URL
    ano = year
    opcao = "opt_04"

    # Crie a conexão com os parâmetros fornecidos
    link = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        "ano": ano,
        "opcao": opcao 
    }

    conection = c.Conection(link, params)
    
    # Extraia a tabela
    table = conection.ExtractTableVitinicultura("comercializacao")

    # Retorne os dados em formato JSON
    return JSONResponse(content=table)



@app.get('/importacao/{year}/{subpot}')
async def ImportExtract(year: str, subopt_01: str):
    
    # Obtenha os parâmetros da URL
    ano = year
    opcao = "opt_05"

    # Crie a conexão com os parâmetros fornecidos
    link = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        "ano": ano,
        "opcao": opcao,
        "subopcao": subopt_01
    }

    conection = c.Conection(link, params)
    
    # Extraia a tabela
    table = conection.ExtractTableVitinicultura("importacao")

    # Retorne os dados em formato JSON
    return JSONResponse(content=table)



@app.get('/Exportacao/{year}/{subpot}')
async def ExportExtract(year: str, subopt_01: str):
    
    # Obtenha os parâmetros da URL
    ano = year
    opcao = "opt_06"

    # Crie a conexão com os parâmetros fornecidos
    link = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
    params = {
        "ano": ano,
        "opcao": opcao,
        "subopcao": subopt_01
    }

    conection = c.Conection(link, params)
    
    # Extraia a tabela
    table = conection.ExtractTableVitinicultura("exportacao")

    # Retorne os dados em formato JSON
    return JSONResponse(content=table)



if __name__ == '__main__':
    uvicorn.run(app)