# Election-BlockChain-PHE

![image](https://github.com/qasim12343/Election-BlockChain-PHE/assets/93463121/8c0741d4-cfd9-48d3-8834-2edc52362209)
![c](https://github.com/qasim12343/Election-BlockChain-PHE/assets/93463121/a5718470-ad46-4148-89d4-666edd8a468c)

- It is implementation of election that people would vote for side A(+1) or B(-1).
- Voting is based on local Blockchain(city) and global blockchain(country).
- Pailler Homomorphic Encryption used for secret computation.

  
## Details

Blockchains enable city-wide elections. While the total of these local blockchains in the form of blocks or nodes within the Country blockchain show the elections in a country.
Node or Block in the local blockchain represents the vote of a person in that city.
Node or Block in the blockchain of a country represents the result of the votes obtained from each city.
Each person's vote is recorded in encrypted form in local blockchains.
Pailler encryption enables the votes registered in each city to be calculated in an encrypted form (without revealing the final value), then the result is transferred to the national blockchain.
Finally, all the votes collected from the cities are calculated in an encrypted form, and as a result, they are decrypted with a private key and the winner is announced.


## Requirements

- PHE Library to install "pip install phe".
