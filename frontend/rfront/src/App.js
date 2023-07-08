import "./App.css";
import React from "react";
import useWebSocket, { ReadyState } from "react-use-websocket";
import axios from "axios";

const SendWebSocketComponent = () => {
  const messageHistory = React.useRef([]);

  // Connection URL - connect to the server on localhost at port 9000
  const connectionUrl = "ws://localhost:9000";

  const { sendMessage, lastMessage, readyState } = useWebSocket(connectionUrl);

  // Handle messages, appending them to the message history
  React.useEffect(() => {
    if (lastMessage !== null) {
      messageHistory.current = [...messageHistory.current, lastMessage];
    }
  }, [lastMessage]);

  // Event handler for sending messages
  const handleClickSendMessageButton = React.useCallback(
    () => sendMessage(`Hello from WebSocket at port 9000`),
    []
  );

  // Interface elements
  return (
    <div>
      <button
        onClick={handleClickSendMessageButton}
        disabled={readyState !== ReadyState.OPEN}
      >
        Click me to send 'Hello from WebSocket at port 9000'
      </button>

      {lastMessage ? (
        <p>Last received message: {lastMessage.data}</p>
      ) : (
        <p>No message received yet.</p>
      )}
    </div>
  );
};

const WebSocketComponent = () => {
  const [data, setData] = React.useState(null);
  const [ws, setWs] = React.useState(null);

  const waitData = async () => {
    try {
      const response = await axios.get(
        "http://localhost:9001/wait?dirname=test0"
      );
      //   setData(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  React.useEffect(() => {
    const websocket = new WebSocket("ws://localhost:9000/websocket-endpoint");
    setWs(websocket);
    websocket.onopen = () => {
      console.log("connected");
    };
    websocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log(data);
      setData(JSON.stringify(data));
    };
    websocket.onclose = () => {
      console.log("disconnected");
      // automatically try to reconnect on connection loss
      setWs(new WebSocket("ws://localhost:9000/websocket-endpoint"));
    };

    return () => {};
  }, []);

  return (
    <div>
      <p>Data from WebSocket: {data}</p>
      <button onClick={waitData}>Wait Data</button>
    </div>
  );
};

const baseURL = "http://localhost:3000";

function FetchButton() {
  const [data, setData] = React.useState(null);

  const fetchData = async () => {
    try {
      const response = await axios.get(
        "http://localhost:3000/read?dirname=test0"
      );
      setData(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  React.useEffect(() => {
    fetchData();
    const intervalId = setInterval(fetchData, 1000); // fetch data every 1 second

    // Clean up function to clear the interval when the component unmounts
    return () => clearInterval(intervalId);
  }, []); // Empty dependency array means this effect runs once on mount and clean up on unmount

  return (
    <div>
      <button onClick={fetchData}>Fetch Data</button>

      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
    </div>
  );
}

let dummy = ({ num }) => {
  <>{num}</>;
};

function MyComponent(props) {
  return (
    <div>
      <p>Prop 1: {props.prop1}</p>
      <p>Prop 2: {props.prop2}</p>
    </div>
  );
}

function Square(dictionary) {
  async function handleClick() {
    let response = await axios.get(`${baseURL}/read?dirname=test`);
    console.log(response.data);
    console.log("clicked!");
  }

  return (
    <>
      <button className="square" onClick={handleClick}>
        {dictionary.data}
      </button>
      <button className="square" onClick={handleClick}>
        {dictionary.data}
      </button>
    </>
  );
}

function Board() {
  return (
    <>
      {/* <MyComponent prop1="value1" prop2="value2" /> */}
      <SendWebSocketComponent />
      <WebSocketComponent />
      <FetchButton />
      {/* <div className="board-row">
        <Square key1="1" key2="1" />
        <Square />
        <Square />
      </div>
      <div className="board-row">
        <Square />
        <Square />
        <Square />
      </div>
      <div className="board-row">
        <Square />
        <Square />
        <Square />
      </div> */}
    </>
  );
}

function App() {
  return <div className="App">{Board()}</div>;
}

export default App;
