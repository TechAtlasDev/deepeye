export default function Cuerpo({ resultados }) {
	return (
		<div className="flex w-full h-full p-10">
			<h2>Cantidad de resultados encontrados por Shodan: {resultados}</h2>
		</div>
	);
}