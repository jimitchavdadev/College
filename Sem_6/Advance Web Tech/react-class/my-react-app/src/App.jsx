import React from "react";

class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  increment = () => {
    this.setState({ count: this.state.count + 1 });
  };

  decrement = () => {
    this.setState({ count: this.state.count - 1 });
  };

  reset = () => {
    this.setState({ count: 0 });
  };

  render() {
    return (
      <div >
        <h1 >Counter: {this.state.count}</h1>
        <button
          onClick={this.increment}
        >
          Increment
        </button>
        <button
          onClick={this.decrement}
        >
          Decrement
        </button>
        <button
          onClick={this.reset}
        >
          Reset
        </button>
      </div>
    );
  }
}

export default function App() {
  return (
    <div className="flex items-center min-h-screen bg-gray-100">
      <Counter />
    </div>
  );
} 