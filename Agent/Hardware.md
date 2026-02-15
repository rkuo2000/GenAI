## 硬體比較

### RPi5 vs RPi4
| 項目              | Raspberry Pi 5          | Raspberry Pi 4 Model B      | 差異重點             |
| --------------- | ----------------------- | --------------------------- | ---------------- |
| 🧠 **CPU**      | 四核 2.4 GHz Cortex-A76   | 四核 1.8 GHz Cortex-A72       | 🚀 約 2–3× 效能提升   |
| 🎮 **GPU**      | VideoCore VII @ 1.1 GHz | VideoCore VI @ 800 MHz      | 🎨 圖形效能更強        |
| 🧮 **RAM**      | 4GB / 8GB LPDDR4X-4267  | 2GB / 4GB / 8GB LPDDR4-3200 | ⚡ 記憶體頻寬更高        |
| 🖥 **顯示輸出**     | 雙 micro-HDMI（雙 4Kp60）   | 雙 micro-HDMI（單 4Kp60）       | 🖥️ 多螢幕能力提升      |
| 📷 **相機 / DSI** | 2 × 4-lane MIPI         | 1 × 2-lane CSI + 1 × DSI    | 📸 支援雙鏡頭         |
| 💾 **PCIe**     | 1 × PCIe 2.0            | ❌ 無                         | 🚀 可接 NVMe / SSD |
| 🔌 **USB**      | 2× USB3 + 2× USB2       | 2× USB3 + 2× USB2           | ➖ 相同             |
| 🔋 **電源**       | 5V / 5A USB-C PD        | 5V / 3A USB-C               | ⚠️ Pi 5 需更高功率    |
| ⭐ **新功能**       | 電源按鈕、RTC                | 無                           | 👍 使用更方便         |
| 🔧 **I/O 架構**   | RP1 I/O 控制器             | SoC 內建 I/O                  | 📈 I/O 效能更佳      |

---
### Mac mini-M4 OrinNano-Super vs K230
| Feature               | NVIDIA Jetson Orin Nano Super            | Kendryte K230 (CanMV / 01Studio)  |
| --------------------- | ---------------------------------------- | --------------------------------- |
| 🎯 **Primary Focus**  | High-performance Edge AI / Generative AI | Ultra-low-power Vision / Audio AI |
| 🧠 **AI Performance** | Up to **67 TOPS (INT8)**                 | ~**6 TOPS (INT8)**                |
| 🏗 **Architecture**   | ARM Cortex-A78AE + Ampere GPU            | Dual-core RISC-V (C908 + C908V)   |
| 💻 **CPU**            | 1.7GHz 6-core ARM Cortex-A78AE           | 1.6 GHz RISC-V + 800 MHz RISC-V   |
| 🎮 **GPU**            | 1024-core NVIDIA Ampere GPU              | ❌ None (vector processing only)   |
| 🧮 **RAM**            | 8 GB LPDDR5                              | 512 MB – 1 GB LPDDR3/4            |
| 💾 **Storage**        | M.2 NVMe SSD (PCIe)                      | microSD Card                      |
| 🔋 **Power Budget**   | 7W – 25W (configurable)                  | Very low (battery-friendly)       |
| 🧰 **Software Stack** | JetPack SDK, CUDA, TensorRT              | CanMV (MicroPython), RT-Smart     |
| 💵 **Price**          | ~$249 USD (Dev Kit)                      | ~$25 – $55 USD                    |

---
### Mac M4 Pro vs Jetson Orin 64GB
| Feature                   | Apple M4 Pro (20-core GPU)                          | Jetson AGX Orin 64GB               |
| ------------------------- | --------------------------------------------------- | ---------------------------------- |
| **GPU Architecture**      | Custom Apple GPU architecture                       | NVIDIA Ampere architecture         |
| **GPU Cores**             | 20 GPU cores (~2,560 shading units est.)            | 2,048 CUDA cores + 64 Tensor Cores |
| **GPU Clock Speed**       | Up to ~1.8 GHz                                      | Up to ~1.3 GHz                     |
| **Memory**                | Unified memory up to 64 GB, 273 GB/s bandwidth      | 64 GB LPDDR5, 204.8 GB/s bandwidth |
| **AI Performance**        | Not publicly specified (uses 16-core Neural Engine) | Up to **275 TOPS (INT8)**          |
| **Ray Tracing**           | Hardware-accelerated ray tracing                    | Hardware ray-tracing support       |
| **Manufacturing Process** | 3 nm                                                | 8 nm                               |
| **Power Consumption**     | ~32 W (estimated)                                   | Configurable 15 W – 60 W           |
