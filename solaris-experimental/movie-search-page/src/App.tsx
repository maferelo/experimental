import { memo, useEffect, useMemo, useState } from "react";
import "./styles.css";

const PokemonList = ({ pokemons }) => {
  return pokemons.map((pokemon) => (
    <div key={pokemon.name}>{pokemon.name}</div>
  ));
};

const PokemonListMemo = memo(PokemonList);

let appRender = 0;
export default function App() {
  console.log(`appRender = ${appRender++}`);
  const [pokemons, setPokemons] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
      .then((res) => res.json())
      .then((res) => {
        setPokemons(res.results);
      });
  }, []);

  const filteredPokemons = useMemo(() => {
    return pokemons.filter((pokemon) => pokemon.name.includes(search));
  }, [pokemons, search]);

  return (
    <>
      <input
        type="text"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
      <PokemonListMemo pokemons={filteredPokemons} />
    </>
  );
}
