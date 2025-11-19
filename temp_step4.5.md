#### 🎯 What Generator Should Create

**For ALL Specification Toolkits (including yours)**:

| Component | Purpose | Example |
|-----------|---------|---------|
| **Project Structure** | Standardized directories | `.{toolkit}/`, `memory/`, `specs/` |
| **Constitution** | Project principles | `memory/constitution.md` |
| **Specification Templates** | Starter spec files | `campaign-spec.yaml`, `product-spec.yaml` |
| **README** | Project documentation | `README.md` with usage guide |
| **Custom Commands** | Optional slash commands | `.{toolkit}/commands/*.md` |

---

#### 🚨 Common Misunderstanding

**⚠️ WARNING: "Content Generation" confusion**

```
❌ WRONG Interpretation:
Use Case: "AI-Driven Content Generation"
→ Thinking: "Generate marketing posts/blogs"
→ Generator creates: Domain content (posts, articles)
→ Result: Violates MetaSpec architecture

✅ CORRECT Interpretation:
Use Case: "AI-Driven Content Generation"
→ Thinking: "Help users generate specifications with AI"
→ Generator creates: Project structure for specs
→ Result: Follows MetaSpec pattern
```

**Key principle**: 
- Specification Toolkits generate **PROJECT FILES** to manage specs
- Domain content generation (posts, docs) belongs in **separate applications** that consume specs

---

#### ✅ Real Example: marketing-spec-kit

```yaml
Use Cases:
  1. Parse marketing specifications
  2. Validate campaign structures  
  3. AI-Driven Content Generation ⚠️

Correct Generator behavior:
  ✅ Generate: Project directory structure
  ✅ Generate: Specification templates (campaign.yaml)
  ✅ Generate: Constitution.md
  ✅ Generate: README.md
  
  ❌ Do NOT generate: Marketing posts
  ❌ Do NOT generate: Blog articles
  ❌ Do NOT generate: Social media content
  
  (Those belong in a separate "marketing-content-generator" application)
```

---

