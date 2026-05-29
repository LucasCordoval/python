import requests
from flask import Flask, render_template, request
import math as mt

def calcular():
    operacao = request.form['operacao']
    resultado = ""
    resultado2 = ""
    etapas = ""
    if operacao == 'BHASKARA':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        num3 = float(request.form['num3'])
        if num1 == 0:
            resultado = "Deve ser diferente de 0" 
            resultado2 = "N/A"
        else:
            delta = (num2 ** 2) - 4 * num1 * num3
            if delta < 0:
                print("Sem resultado real")
            else:
                resultado = (( -1 * num2) +  mt.sqrt(delta)) / (2 * num1)
                resultado2 = (( -1 * num2) -  mt.sqrt(delta)) / (2 * num1)
                etapas = f'Raízes encontradas: {resultado} e {resultado2}'

    else:
        num1 = float(request.form['num1'])
        operacao = request.form['operacao']
        if operacao == 'sqrt':
            if num1 < 0:
                print("erro")
            else:
                resultado =  mt.sqrt(num1)
                etapas = f'{mt.sqrt(num1)}'
        else:       
            num2 = float(request.form['num2'])

            if operacao == '+':
                resultado = num1 + num2
                etapas = f'{num1} + {num2} = {resultado}'
            elif operacao == '-':
                resultado = num1 - num2
                etapas = f'{num1} - {num2} = {resultado}'
            elif operacao == '*':
                resultado = num1 * num2
                etapas = f'{num1} * {num2} = {resultado}'
            elif operacao == '/':
                if num2 != 0:
                    resultado = num1 / num2
                    etapas = f'{num1} / {num2} = {resultado}'
            elif operacao == '**':
                resultado = num1 ** num2
                etapas = f'{num1} ** {num2} = {resultado}'
            elif operacao == 'log':
                resultado = mt.log(num1, num2)
                etapas = f'log_{num2}({num1}) = {resultado}'
            else:
                resultado = 'Operação inválida'
                etapas = 'A operação selecionada é inválida.'
        
    return render_template('calculadora.html', etapas=etapas, resultado=resultado, resultado2=resultado2)
