import { useState, useEffect, process } from "react";
import "./App.css";

export default function App() {
  const [secretarias, setSecretarias] = useState([]);

  // --- 1. States para os campos do nosso formulário ---
  const [nome, setNome] = useState("");
  const [sigla, setSigla] = useState("");
  const [secretario, setSecretario] = useState("");
  // ---------------------------------------------------

  const apiUrl = import.meta.env.VITE_API_URL;

  // Efeito para buscar a lista inicial de secretarias
  useEffect(() => {
    fetch(apiUrl + "/secretarias")
      .then((response) => response.json())
      .then((data) => setSecretarias(data))
      .catch((error) => console.error("Erro ao buscar dados:", error));
  }, []);

  // --- 2. Função para lidar com o envio do formulário ---
  const handleSubmit = (event) => {
    event.preventDefault(); // Impede que a página recarregue ao enviar
    const novaSecretaria = { nome, sigla, secretario };
    fetch(apiUrl + "/secretarias", {
      method: "POST", // Usamos o método POST
      headers: {
        "Content-Type": "application/json", // Dizemos que estamos enviando JSON
      },
      body: JSON.stringify(novaSecretaria), // Convertemos nosso objeto para texto JSON
    })
      .then((response) => response.json())
      .then((data) => {
        // 3. Adiciona a nova secretaria à lista existente, sem recarregar a página!
        setSecretarias([...secretarias, data]);
        // Limpa os campos do formulário
        setNome("");
        setSigla("");
        setSecretario("");
      })
      .catch((error) => console.error("Erro ao criar secretaria:", error));
  };

  const handleDelete = (id) => {
    fetch(`${apiUrl}/secretarias/${id}`, {
      method: "DELETE",
    })
    .then(response => {
      if (response.ok) {
        setSecretarias(secretarias.filter(secretaria => secretaria.id != id))
      } else {
        console.error("Falha ao deletar secretaria.");
      }
    })
    .catch(error => console.error("Erro ao deletar secretaria: ", error));
  }

  // ----------------------------------------------------
  return (
    <main>
      <h1>Controle de Secretarias</h1>

      {/* --- 4. Nosso formulário --- */}
      <form onSubmit={handleSubmit}>
        <h2>Adicionar Nova Secretaria</h2>
        <input
          type="text"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
          placeholder="Nome da Secretaria"
          required
        />
        <input
          type="text"
          value={sigla}
          onChange={(e) => setSigla(e.target.value)}
          placeholder="Sigla"
          required
        />
        <input
          type="text"
          value={secretario}
          onChange={(e) => setSecretario(e.target.value)}
          placeholder="Nome do Secretário"
          required
        />
        <button type="submit">Salvar</button>
      </form>
      {/* --------------------------- */}

      <h2>Secretarias Cadastradas</h2>
      <ul>
        {secretarias.map((secretaria) => (
            <li key={secretaria.id}>
              {secretaria.nome} ({secretaria.sigla}) - Secretário:{" "}
              {secretaria.secretario}
              <button onClick={() => handleDelete(secretaria.id)}>Deletar</button>
            </li>
        ))}
      </ul>
    </main>
  );
}
