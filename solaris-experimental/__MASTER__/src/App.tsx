import React, {
  useCallback,
  useEffect,
  useMemo,
  useReducer,
  useRef,
  useState,
} from "react";
import { Pokemon, getByName } from "./API";

import "./styles.css";

interface PokemonWithPower extends Pokemon {
  power: number;
}

const calculatePower = (pokemon: Pokemon) =>
  pokemon.hp +
  pokemon.attack +
  pokemon.defense +
  pokemon.special_attack +
  pokemon.special_defense +
  pokemon.speed;

let tableRender = 0;
const PokemonTable: React.FunctionComponent<{
  pokemon: PokemonWithPower[];
}> = ({ pokemon }) => {
  console.log(`tableRender = ${tableRender++}`);
  return (
    <table>
      <thead>
        <tr>
          <td>ID</td>
          <td>Name</td>
          <td>Type</td>
          <td colSpan={6}>Stats</td>
          <td>Power</td>
        </tr>
      </thead>
      <tbody>
        {pokemon.map((p) => (
          <tr key={p.id}>
            <td>{p.id}</td>
            <td>{p.name}</td>
            <td>{p.type.join(",")}</td>
            <td>{p.hp}</td>
            <td>{p.attack}</td>
            <td>{p.defense}</td>
            <td>{p.special_attack}</td>
            <td>{p.special_defense}</td>
            <td>{p.speed}</td>
            <td>{p.power}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

const MemoedPokemonTable = React.memo(PokemonTable);

interface CounterState {
  count: number;
}

interface CounterAction {
  type: "increment";
}

const counterInitialState = { count: 0 };

const timerReducer = (state: CounterState, action: CounterAction) => {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    default:
      return state;
  }
};

let appRender = 0;
export default function App() {
  console.log(`appRender = ${appRender++}`);
  const [pokemon, setPokemon] = useState<Pokemon[]>([]);
  const [tooltipShown, setTooltipShown] = useState<boolean>(false);
  const [time, setTime] = useState<number>(0);
  const [counterState, dispatch] = useReducer(
    timerReducer,
    counterInitialState
  );
  const tooltipRef = useRef<HTMLDivElement>(null);

  const increment = () => {
    dispatch({ type: "increment" });
  };

  const [search, setSearch] = useState("");
  const onSetSearch = useCallback(
    (evt: React.ChangeEvent<HTMLInputElement>) => setSearch(evt.target.value),
    []
  );

  useEffect(() => {
    getByName(search).then(setPokemon);
  }, [search]);

  const onMouseEnter = useCallback(() => {
    setTooltipShown(true);
  }, []);
  const onMouseLeave = useCallback(() => {
    setTooltipShown(false);
  }, []);

  useEffect(() => {
    const tooltip = tooltipRef.current;
    tooltip?.addEventListener("mouseenter", onMouseEnter);
    tooltip?.addEventListener("mouseleave", onMouseLeave);
    return () => {
      tooltip?.removeEventListener("mouseenter", onMouseEnter);
      tooltip?.removeEventListener("mouseleave", onMouseLeave);
    };
  }, [onMouseEnter, onMouseLeave]);

  const pokemonWithPower = useMemo(
    () =>
      pokemon.map((p) => ({
        ...p,
        power: calculatePower(p),
      })),
    [pokemon]
  );

  const [threshold, setThreshold] = useState(0);
  const onSetThreshold = useCallback(
    (evt: React.ChangeEvent<HTMLInputElement>) =>
      setThreshold(parseInt(evt.target.value, 10)),
    []
  );

  const countOverThreshold = useMemo(
    () => pokemonWithPower.filter((p) => p.power > threshold).length,
    [pokemonWithPower, threshold]
  );

  const min = useMemo(
    () => Math.min(...pokemonWithPower.map((p) => p.power)),
    [pokemonWithPower]
  );
  const max = useMemo(
    () => Math.max(...pokemonWithPower.map((p) => p.power)),
    [pokemonWithPower]
  );

  useEffect(() => {
    const interval = setInterval(() => {
      setTime((t) => t + 1);
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <div className="top-bar">
        <div>Search</div>
        <input type="text" value={search} onChange={onSetSearch}></input>
        <div>Power threshold</div>
        <input type="text" value={threshold} onChange={onSetThreshold}></input>
        <div>Count over threshold: {countOverThreshold}</div>
        <div ref={tooltipRef}>Tooltip popper</div>
        {tooltipShown && <div>I am the tooltip</div>}
        <div>Time: {time}</div>
        <div>Counter: {counterState.count}</div>
        <button onClick={increment}>Increment</button>
      </div>
      <div className="top-bar">
        <div>Min: {min}</div>
        <div>Max: {max}</div>
      </div>
      <div className="two-column">
        <MemoedPokemonTable pokemon={pokemonWithPower} />
      </div>
    </div>
  );
}
