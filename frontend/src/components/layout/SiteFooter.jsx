import { FaEnvelope, FaLinkedin, FaPhone } from "react-icons/fa";
import { SiZalo } from "react-icons/si";

export default function SiteFooter() {
  return (
    <footer className="mt-20 border-t border-zinc-800 py-8 text-sm text-zinc-400">
      <div className="flex flex-col items-center gap-4 sm:flex-row sm:justify-between">
        <div className="flex flex-col items-center gap-3 sm:items-start">
          <div className="flex items-center justify-center gap-5">
            <a
              href="mailto:hello@example.com"
              className="inline-flex items-center gap-2 hover:text-blue-300"
            >
              <FaEnvelope />
              hello@example.com
            </a>
            <a
              href="tel:+1234567890"
              className="inline-flex items-center gap-2 hover:text-blue-300"
            >
              <FaPhone />
              +1 (234) 567-890
            </a>
          </div>

          <div className="flex items-center justify-center gap-5">
            <a
              href="#"
              className="inline-flex items-center gap-2 hover:text-blue-300"
            >
              <FaLinkedin />
              LinkedIn
            </a>
            <a
              href="#"
              className="inline-flex items-center gap-2 hover:text-blue-300"
            >
              <SiZalo />
              Zalo
            </a>
          </div>
        </div>
        <p className="text-center sm:text-right">
          © 2026 AITeach. All rights reserved.
        </p>
      </div>
    </footer>
  );
}
