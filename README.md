# The Quantum Writing Prompt Generator
A writing prompt generator for the Gotham Writers Workshop game show

<img src="https://www.radhapyarisandhir.com/wp-content/uploads/2020/11/gotham-prompt-generator-header.jpg" width="80%"  />

## Overview
This tool randomly generates a story prompt by making use of quantum computing.

##  How to Use The D&D μStarter Kit

An online version is provided at [promptgen.herokuapp.com](https://promptgen.herokuapp.com/). This version runs only on the QASM simulator so that the server is not overloaded.

### Navigating The Quantum Writing Prompt Generator

<img src="https://www.radhapyarisandhir.com/wp-content/uploads/2020/12/Gotham-Prompt-Gen-Screenshot.png" width="80%"  />

Click on ‘Refresh’ to generate a new prompt. If the same prompt shows up a number of times, don't worry! This can happen due to cache. Simply click Refresh until you get a new one! 

### How to Run The Quantum Writing Prompt Generator Locally

If you want to run it on a actual quantum device, or just have a local copy of this follow the following step:

1. Clone the git repository from [Github](https://github.com/quantum-kittens/quantum-prompt-generator).
2. `cd` into the git repository.
3. Execute `pip install -r requirements.txt`.
4. Execute `export FLASK_APP=app.py`
5. Execute `flask run`

The app will available at `127.0.0.1:5000/`. You can direct your browser to that location to access it. To run this on an actual quantum device, open `app.py` and edit it as mentioned in the comments in the file, before executing `flask run`.


##  How The Quantum Writing Prompt Generator Works

### Prompt Generation
A prompt is randomly generated by tapping into two phrase banks: CHARACTER and SITUATION. Each prompt takes the form: 

> A \<CHARACTER\> who \<SITUATION\>.
  
For instance, if "grocery store cashier" cashier is pulled from the CHRACTER bank, and "is cut off from family inheritance" is pulled from the SITUATION bank, then the generated prompt becomes:

> A grocery store cashier who is cut off from family inheritance.

Random selection takes place through quantum computing.

### Quantum Computing
Quantum computing is used to randomly select phrases from the phrase banks. 

If a choice needs to be made from among eight word options, say, then a circuit of three qubits is prepared. A Hadamard gate is applied on each qubit, placing them in a superposition of all eight possible states from |000⟩ to |001⟩ and so on to |111⟩. Upon measurement, one of the eight states is obtained, which corresponds to one of the eight word options.

All circuits are simulated with the QASM simulator from IBM’s open source SDK, Qiskit. However if you would rather user IBM's quantum devices then you can do so, as discussed earlier.

This generator works similarly to the [D&D μStarter Kit](https://qdnd.herokuapp.com/). For a more detailed layperson explanation, check out the article ["How I Use Quantum Computing to Play Dungeons & Dragons"](https://medium.com/swlh/how-i-use-quantum-computing-to-play-dungeons-dragons-68528f6befa2).

## Credits
#### Created by:
- Radha Pyari Sandhir (Github: [quantum-kittens](https://github.com/quantum-kittens), Twitter: [RadhaPyari](https://twitter.com/RadhaPyari))
- Soham Pal (Github: [e-eight](https://github.com/e-eight), Twitter: [dragonbornmonk](https://twitter.com/dragonbornmonk))

#### Prompts from:
- Josh Sippie (Twitter: [sippenator101](https://twitter.com/sippenator101)
- Gotham Writers Workshop (Website: [writingclasses.com](https://www.writingclasses.com/)) 

#### Quantum Resources: 
- [The Quantum Catalog](http://quantumcatalog.com/)
- [Qiskit](https://qiskit.org/)


Cover photo by [Amador Loureiro on Unsplash](https://unsplash.com/@amadorloureiroblanco).


