# IDS2935 Design Challenge 2
For this design challenge, the purple group is designing an app to assist those with difficulty socializing

## Build
### Linux
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### Windows
```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## App Flowchart
```mermaid
flowchart TD
    A[wait for microphone input] --voice differentation--> B[seperate voices into speakers]
    B --> E[Speech to text]
    E --sentence finished--> C[Run conversation against LLM]
    C --> D[Provide 3 conversation options]
    D-->A
```

## Voice Differentiation Flowchart (Not yet implemented)
```mermaid
flowchart TD
    A[Wait for microphone input] --> B[Run current voice differentation network on waveform]
    A --> C[Temporarily store waveform in volatile memory]
    C --> D[Retrain voice differentiation network in place]
    B --> E[Output ID of who is talking]
    E --> A
        D --> A

```

