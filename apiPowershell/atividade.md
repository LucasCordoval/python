PS C:\Users\lucas> Invoke-RestMethod http://127.0.0.1:5000/api/livros/5 `
>>    -Method DELETE `
>>    -ContentType "application/json" `
>>
PS C:\Users\lucas> Invoke-RestMethod http://127.0.0.1:5000/api/livros/6 `
>>    -Method DELETE `
>>    -ContentType "application/json" `
>>

PS C:\Users\lucas> Invoke-RestMethod http://127.0.0.1:5000/api/livros/7 `
>>    -Method DELETE `
>>    -ContentType "application/json" `
>>

PS C:\Users\lucas> Invoke-RestMethod http://127.0.0.1:5000/api/livros/5 `
>>   -Method PUT `
>>  -ContentType "application/json" ` -Body '{"titulo":"Dom Casmurro","autor":"Machado de Assis","ano":1900}'


ano          : 1900
autor        : Machado de Assis
data_criacao : 2026-07-28 20:14:21.745414
id           : 5
titulo       : Dom Casmurro