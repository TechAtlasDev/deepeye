"use client"

import Barra from "./Barra_lateral";
import Cuerpo from "./Cuerpo";

import { useState } from "react";

export default function DashboardComponent() {
  const [resultados, setResultados] = useState([]);
  return (
    <main class="flex flex-row h-screen w-screen">
      <Barra setResultados={setResultados} />
      <Cuerpo resultados={resultados} />
    </main>
  );
}