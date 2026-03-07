# Context Engineering Outline

## สอนเพื่อนทำ Context Engineering

> "Most agent failures aren't model failures — they're context failures."

---

## 1. ทำไมต้อง Context Engineering?

### 1.1 ปัญหาของ Vibe Coding
- พิมพ์ prompt แบบลอย ๆ ได้ผลลัพธ์ไม่แน่นอน
- AI ไม่รู้จัก codebase, conventions, หรือ architecture ของเรา
- ต้องแก้งานซ้ำแล้วซ้ำเล่า

### 1.2 Prompt Engineering vs Context Engineering

| | Prompt Engineering | Context Engineering |
|---|---|---|
| **แนวคิด** | เน้นการเขียน prompt ให้เก่ง | เน้นการจัดเตรียม context ทั้งระบบ |
| **เปรียบเทียบ** | เหมือนเขียนโน้ตแปะ | เหมือนเขียนบทละครทั้งเรื่อง |
| **ผลลัพธ์** | ได้ผลบางครั้ง | ได้ผลสม่ำเสมอ |

### 1.3 ประโยชน์ของ Context Engineering
- ลด AI failures อย่างมาก
- ได้โค้ดที่ consistent ตาม project patterns
- รองรับ feature ที่ซับซ้อนได้
- มี self-correcting loop (AI แก้ไขตัวเองได้)

---

## 2. องค์ประกอบหลักของ Context Engineering

### 2.1 CLAUDE.md — กฎและ conventions ของโปรเจกต์
- Project awareness & context (อ่าน PLANNING.md, TASK.md)
- Code structure & modularity (แบ่งไฟล์, จำกัดความยาว)
- Testing & reliability (Pytest, test patterns)
- Style & conventions (PEP8, type hints, docstrings)
- AI behavior rules (ห้าม hallucinate, ห้ามลบโค้ดเอง)

### 2.2 INITIAL.md — คำอธิบาย feature ที่ต้องการ
- **FEATURE**: อธิบาย feature ให้ชัดเจนและเฉพาะเจาะจง
- **EXAMPLES**: ชี้ไปที่ตัวอย่างโค้ดใน `examples/`
- **DOCUMENTATION**: ลิงก์เอกสาร API, library, MCP server
- **OTHER CONSIDERATIONS**: gotchas, ข้อจำกัด, ข้อควรระวัง

### 2.3 Examples — ตัวอย่างโค้ดที่ AI ใช้เป็นแบบ
- Code structure patterns
- Testing patterns
- Integration patterns
- ยิ่งมี examples เยอะ = ผลลัพธ์ยิ่งดี

### 2.4 PRPs (Product Requirements Prompts) — พิมพ์เขียวการ implement
- เหมือน PRD แต่ออกแบบมาสำหรับ AI โดยเฉพาะ
- มี implementation steps + validation gates
- มี error handling patterns + test requirements

---

## 3. Workflow แบบ Step-by-Step

### 3.1 ตั้งค่าโปรเจกต์
```
project/
├── CLAUDE.md              # กฎของโปรเจกต์
├── INITIAL.md             # คำอธิบาย feature
├── examples/              # ตัวอย่างโค้ด
├── PRPs/                  # Product Requirements Prompts
│   └── templates/
│       └── prp_base.md    # Template สำหรับ PRP
└── .claude/
    └── commands/          # Custom slash commands
        ├── generate-prp.md
        └── execute-prp.md
```

### 3.2 เขียน CLAUDE.md
- กำหนด rules ที่ AI ต้องทำตามทุกครั้ง
- ใส่ conventions เฉพาะโปรเจกต์
- กำหนดมาตรฐาน testing และ documentation

### 3.3 เขียน INITIAL.md
- อธิบาย feature ให้ละเอียด
- เตรียม examples ใน `examples/` folder
- รวบรวม documentation links
- ระบุ gotchas และข้อควรระวัง

### 3.4 Generate PRP
```bash
/generate-prp INITIAL.md
```
- AI อ่าน feature request → วิเคราะห์ codebase → ค้นหา docs → สร้าง PRP

### 3.5 Execute PRP
```bash
/execute-prp PRPs/your-feature-name.md
```
- AI อ่าน PRP → วางแผน → implement → test → แก้ไข → เสร็จสิ้น

---

## 4. เทคนิคการเขียน INITIAL.md ให้ดี

### 4.1 เขียน FEATURE ให้เฉพาะเจาะจง
- ❌ `"สร้าง web scraper"`
- ✅ `"สร้าง async web scraper ด้วย BeautifulSoup ที่ดึงข้อมูลสินค้า, จัดการ rate limiting, และเก็บข้อมูลใน PostgreSQL"`

### 4.2 เตรียม Examples ที่ดี
- ใส่ code patterns ที่อยากให้ AI ทำตาม
- แสดงทั้ง "ควรทำ" และ "ไม่ควรทำ"
- รวม error handling patterns

### 4.3 ใส่ Documentation ให้ครบ
- Official API docs
- Library documentation
- MCP server resources

### 4.4 ระบุ Other Considerations
- Authentication requirements
- Rate limits
- Performance requirements
- Common pitfalls ที่ AI มักพลาด

---

## 5. Use Cases ที่เหมาะกับ Context Engineering

### 5.1 สร้างโปรเจกต์ใหม่ (New Project)
- ใช้ CE-Starter-Kit-for-New-Project
- วางรากฐาน architecture ตั้งแต่เริ่มต้น

### 5.2 ปรับปรุงโปรเจกต์เดิม (Optimize Existing)
- ใช้ CE-Starter-Kit-for-Optimize
- เพิ่ม context engineering เข้าไปใน codebase ที่มีอยู่

### 5.3 สร้าง AI Agents
- แบ่งเป็น agent.py / tools.py / prompts.py
- ใช้ PRP กำหนด agent behavior อย่างละเอียด

### 5.4 สร้าง Full-Stack Applications
- กำหนด frontend + backend conventions ใน CLAUDE.md
- ใช้ examples แสดง integration patterns

---

## 6. Best Practices

### 6.1 ชัดเจน ≠ ยาว
- เขียนให้ specific แต่กระชับ
- ทุก rule ใน CLAUDE.md ต้องมีเหตุผล

### 6.2 ให้ Examples เยอะ ๆ
- AI เรียนรู้จาก patterns ได้ดีมาก
- ยิ่งเห็นตัวอย่างเยอะ ยิ่ง implement ได้ตรง

### 6.3 ใช้ Validation Gates
- ใส่ test commands ที่ต้อง pass ใน PRP
- AI จะ iterate จนกว่า validations จะผ่านทั้งหมด

### 6.4 Iterate และปรับปรุง
- CLAUDE.md ไม่ใช่เขียนครั้งเดียวจบ
- เพิ่ม rules ใหม่เมื่อเจอปัญหาซ้ำ ๆ
- ลบ rules ที่ไม่จำเป็นออก

---

## 7. สรุป

> Context Engineering = การเตรียม **ข้อมูลทั้งหมด** ที่ AI ต้องการ เพื่อให้ทำงานได้ **ถูกต้องตั้งแต่ครั้งแรก**

### Key Takeaways
1. **Context > Prompt** — ให้ context ดีกว่าเขียน prompt เก่ง
2. **CLAUDE.md** — กฎที่ AI ต้องทำตามทุกครั้ง
3. **INITIAL.md** — อธิบาย feature ให้ชัด + examples + docs
4. **PRP** — พิมพ์เขียวที่ AI ใช้ implement
5. **Validation** — ให้ AI ตรวจสอบและแก้ไขตัวเอง
6. **Iterate** — ปรับปรุง context อย่างต่อเนื่อง
