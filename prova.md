Certo! Ecco il contenuto che ti ho fornito, direttamente in formato **Markdown (.md)**. Puoi copiarlo e salvarlo come file `nmap_cheatsheet.md` oppure qualsiasi altro nome tu preferisca con estensione `.md`.

---

### ✅ File Markdown completo:

```markdown
# 🛠️ NMAP Port Scan Cheatsheet

Eseguire uno scan a velocità normale può attivare sistemi IDS (Intrusion Detection System) o altre misure di sicurezza. È ragionevole controllare la velocità dello scan.  
Nmap offre sei template di timing:

- `paranoid` (0)
- `sneaky` (1)
- `polite` (2)
- `normal` (3)
- `aggressive` (4)
- `insane` (5)

Puoi selezionare il template usando il parametro `-T` seguito dal nome o numero:
```bash
nmap -T0 192.168.1.1    # Molto lento
nmap -T paranoid 192.168.1.1
```

---

## 🔍 Comandi Principali

```bash
| nmap -vv -A -p- 10.10.246.8 | Scan completo su tutte e 65535 le porte ``` 

---

## ⚡ Faster Port Scan Alternatives

Se vuoi velocizzare lo scan manuale puoi utilizzare tool come Threader3000:

```bash
python3 threader3000/threader3000.py <IP>
```

Questo script permette di effettuare scansione veloce delle porte comuni e supporta l'uso di script Nmap successivamente.

---

## ✅ Note Utili

- Usa `-oN <file>` per salvare l’output in formato leggibile.
- Usa `grep` per filtrare risultati direttamente dal terminale.
- Per evitare di generare traffico sospetto usa `-T polite` o inferiore.
- Ricorda sempre di rispettare le policy legali prima di effettuare qualsiasi scan.
```

---

### 📥 Come scaricarlo come file `.md`

1. Apri un editor di testo (come Notepad, VS Code, Sublime Text).
2. Incolla il contenuto qui sopra.
3. Vai su **File > Salva con nome**.
4. Scegli una posizione.
5. Scrivi come nome: `nmap_cheatsheet.md`
6. Seleziona come tipo: **Tutti i file (*.*)**
7. Clicca **Salva**

