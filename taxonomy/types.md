# Type classification (`type`)

An incident can belong to several types at once — real attack chains are composite. Counting is by occurrence, so the totals per type add up to more than the number of records.

| Code | Name | English | Records | Classification notes |
|---|---|---|---|---|
| <a id="gov"></a>`GOV` | Governance & policy | Governance & policy | 65 | Regulation, legislation, law enforcement, vendor policy and defensive-side moves. Records with `kind: policy` mostly live here and are **excluded from incident counts**. |
| <a id="cred"></a>`CRED` | Credential abuse | Credential abuse | 57 | Credentials read, carried out or abused by an agent. The difference from `EXFIL` is that what is lost is the **key**, not the data. |
| <a id="weapon"></a>`WEAPON` | Agent used as a weapon | Agent used as a weapon | 54 | A human **deliberately** uses an agent as an attack tool. The difference from `ROGUE` is whether there is a hostile operator. |
| <a id="ipi"></a>`IPI` | Indirect prompt injection | Indirect prompt injection | 47 | **External content** the agent reads is executed as instructions. The deciding factor is that the injection source is outside the user's control (email, issue, web page, document, dataset). |
| <a id="infra"></a>`INFRA` | Agent infrastructure exposure | Agent infrastructure exposure | 41 | The agent's **runtime infrastructure** is exposed: inference services, vector stores, orchestration platforms, agent gateways. |
| <a id="supply"></a>`SUPPLY` | Supply-chain poisoning | Supply-chain poisoning | 38 | The attack happens on the agent's **dependency chain**: packages, models, plugins, extensions, repositories and the agent's own config files. |
| <a id="mcp"></a>`MCP` | MCP & tool-chain | MCP & tool-chain | 31 | The problem is in the **MCP server, the tool description or the tool-approval mechanism** itself, not in the business system being called. |
| <a id="other"></a>`OTHER` | Other | Other | 24 | Deepfakes, voice cloning, AI-assisted fraud and the like — AI is the means, but the record does not involve agent autonomy. |
| <a id="exfil"></a>`EXFIL` | Data exfiltration | Data exfiltration | 28 | Data actually **leaves** the trust boundary. A demo that gets only as far as "it can read" does not count; there must be an outbound channel. |
| <a id="rogue"></a>`ROGUE` | Rogue agent action | Rogue agent action | 26 | **No attacker.** The agent takes a destructive action on its own while carrying out a normal task. |
| <a id="sandbox"></a>`SANDBOX` | Sandbox escape | Sandbox escape | 24 | The agent breaks through **the execution boundary set for it** (container, VM, approval gate, read-only mount). |
| <a id="eval"></a>`EVAL` | Evaluation-environment breakout | Evaluation-environment breakout | 22 | The breakout happens **inside an evaluation or training environment** and is disclosed by the developer itself. A new category that only reached scale in 2026. |

## Typical attack chains

**`GOV`** Governance & policy

```mermaid
flowchart LR
    A["Regulatory or policy action"]:::entry --> B["Lands on vendors and users"]:::step --> C["Compliance requirements change"]:::impact
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

**`CRED`** Credential abuse

```mermaid
flowchart LR
    A["Credentials left within the agent's reach"]:::entry --> B["The agent takes and calls them"]:::step --> C["Credentials abused"]:::impact
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

**`WEAPON`** Agent used as a weapon

```mermaid
flowchart LR
    A["Attacker + jailbreak prompts"]:::entry --> B["LLM orchestrator drives a cluster of sub-agents"]:::step --> C["Target systems compromised"]:::impact
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

**`IPI`** Indirect prompt injection

```mermaid
flowchart LR
    A["External content<br/>email · document · issue · web page"]:::entry --> B["The agent reads it and executes it as instructions"]:::step --> C["Acts beyond its authority, as the attacker intended"]:::impact
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

**`INFRA`** Agent infrastructure exposure

```mermaid
flowchart LR
    A["Agent infrastructure exposed to the internet"]:::entry --> B["Unauthenticated access"]:::step --> C["RCE / data leak"]:::impact
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

**`SUPPLY`** Supply-chain poisoning

```mermaid
flowchart LR
    A["Poisoned package / repo / agent config"]:::entry --> B["Developer or agent installs it automatically"]:::step --> C["Credential theft and self-propagation"]:::impact
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

**`MCP`** MCP & tool-chain

```mermaid
flowchart LR
    A["Malicious MCP server or tool description"]:::entry --> B["The agent's tool-chain loads and trusts it"]:::step --> C["Unauthorised tool calls"]:::impact
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

**`EXFIL`** Data exfiltration

```mermaid
flowchart LR
    A["Sensitive data the agent can reach"]:::entry --> B["Carried out through a vendor-trusted domain<br/>image rendering · API · proxy"]:::step --> C["Data ends up with the attacker"]:::impact
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

**`ROGUE`** Rogue agent action

```mermaid
flowchart LR
    A["An ordinary task handed to the agent"]:::entry --> B["The agent misreads the situation and escalates on its own"]:::step --> C["A destructive command is executed"]:::impact
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

**`SANDBOX`** Sandbox escape

```mermaid
flowchart LR
    A["Evaluation / container environment"]:::entry --> B["A residual path to the network"]:::step --> C["Escape into real systems"]:::impact
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

**`EVAL`** Evaluation-environment breakout

```mermaid
flowchart LR
    A["Evaluation task and reward signal"]:::entry --> B["The model picks the shortcut"]:::step --> C["Crosses into real systems"]:::impact
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

---

[← Back to home](../README.md) · [Severity](severity.md) · [Confidence](confidence.md)
