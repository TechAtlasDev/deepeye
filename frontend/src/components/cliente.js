export default async function realizar_busqueda({ busqueda }) {
  const url = `http://localhost:8000/buscar?consulta=${busqueda}&resultados=org&cantidad=5`;
  const response = await fetch(url);
  const data = await response.json();
  return data;
}