// Função para fazer uma requisição GET à API
async function fetchData() {
  await fetch('http://localhost:5000/mostrar')
    .then(response => response.json())
    .then(data => {
      console.log(data.mostrar);
      const cell = data.mostrar;
      const tabela = document.getElementById("tabelaElementos");
      tabela.innerHTML = ""; // Limpa a tabela

      for (let i in cell) {
        const row = tabela.insertRow();
        const idCell = row.insertCell();
        const mp10Cell = row.insertCell();
        const mp25Cell = row.insertCell();
        const o3Cell = row.insertCell();
        const coCell = row.insertCell();
        const no2Cell = row.insertCell();
        const so2Cell = row.insertCell();

        idCell.innerHTML = cell[i][0];
        mp10Cell.innerHTML = cell[i][1];
        mp25Cell.innerHTML = cell[i][2];
        o3Cell.innerHTML = cell[i][3];
        coCell.innerHTML = cell[i][4];
        no2Cell.innerHTML = cell[i][5];
        so2Cell.innerHTML = cell[i][6];
      }
    })
    .catch(error => {
      console.log('Ocorreu um erro:', error);
    });
    
    makeGetRequest();
}


async function makeGetRequest() {
  // Função para fazer uma requisição GET à API
  await fetch('http://127.0.0.1:5000/classificacao')
    .then(response => response.json())
    .then(data => {
      console.log(data["classificacao"]); // Exibe a resposta da API no console
      console.log(data["mensagem"]); // Exibe a resposta da classificacao no console
      document.getElementById('messagem-classification').innerHTML= data["mensagem"];
      const media = data["classificacao"];
      const classificacao = document.getElementById("classificacaobd");
      classificacao.innerHTML = `${media[0]}--${media[1]}--${media[2]}--${media[3]}--${media[4]}--${media[5]}`;
      // Insere os dados da API na tabela com id "classifcacobd"
    })
    .catch(error => {
      console.log('Ocorreu um erro:', error);
    });
}


// Função para enviar uma requisição PUT para alterar uma amostra
async function updateSample() {
  const id = document.getElementById("IDInput").value;
  const mp10 = document.getElementById("MP10Input").value;
  const mp25 = document.getElementById("MP25Input").value;
  const o3 = document.getElementById("O3Input").value;
  const co = document.getElementById("COInput").value;
  const no2 = document.getElementById("NO2Input").value;
  const so2 = document.getElementById("SO2Input").value;

  const data = {
    mp10: mp10,
    mp25: mp25,
    o3: o3,
    co: co,
    no2: no2,
    so2: so2
  };

  await fetch(`http://localhost:5000/amostras/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
    console.log(data.message);
    fetchData();
  })
  .catch(error => {
    console.log('Ocorreu um erro:', error);
  });
}


// Função para enviar uma requisição POST para adicionar uma amostra
async function addSample() {
  const id = document.getElementById("IDInput").value;
  const mp10 = document.getElementById("MP10Input").value;
  const mp25 = document.getElementById("MP25Input").value;
  const o3 = document.getElementById("O3Input").value;
  const co = document.getElementById("COInput").value;
  const no2 = document.getElementById("NO2Input").value;
  const so2 = document.getElementById("SO2Input").value;

  const data = {
    id: id,
    mp10: mp10,
    mp25: mp25,
    o3: o3,
    co: co,
    no2: no2,
    so2: so2
  };

  await fetch('http://localhost:5000/amostras', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
    console.log(data.message);
    fetchData();
  })
  .catch(error => {
    console.log('Ocorreu um erro:', error);
  });
}


// Função para enviar uma requisição DELETE para excluir uma amostra
async function deleteSample() {
  const id = document.getElementById("IDInput").value;

  await fetch(`http://localhost:5000/amostras/${id}`, {
    method: 'DELETE'
  })
  .then(response => response.json())
  .then(data => {
    console.log(data.message);
    fetchData();
  })
  .catch(error => {
    console.log('Ocorreu um erro:', error);
  });
}

// Carrega os dados iniciais da tabela
fetchData();