"use client"

import Barra from "./Barra_lateral";
import Cuerpo from "./Cuerpo";

export default function DashboardComponent() {
  return (
    <main class="flex flex-row h-screen w-screen">
      <Barra client:load />
      <Cuerpo />
    </main>
  );
}