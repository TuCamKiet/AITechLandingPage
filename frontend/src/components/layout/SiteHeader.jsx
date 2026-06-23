import { FaBars, FaBrain, FaEnvelope } from "react-icons/fa";

export default function SiteHeader({
  isScrolled,
  menuOpen,
  onToggleMenu,
  onCloseMenu,
}) {
  return (
    <>
      <header
        className={`fixed left-1/2 top-0 z-50 mt-3 flex w-[min(95%,72rem)] -translate-x-1/2 items-center justify-between rounded-2xl border px-4 py-3 backdrop-blur-xl transition-all duration-300 ${isScrolled ? "border-violet-400/30 bg-black/85 shadow-xl shadow-violet-500/10" : "border-slate-800/80 bg-slate-900/70 hover:border-slate-700"}`}
      >
        <div className="flex items-center gap-3">
          <div className="flex h-9 w-9 items-center justify-center rounded-sm bg-linear-to-br from-violet-500 to-violet-700 shadow-lg shadow-violet-500/20">
            <FaBrain className="text-white" />
          </div>
          <span className="text-lg font-semibold tracking-wide">AITeach</span>
        </div>

        <nav className="hidden items-center gap-6 text-sm text-slate-300 md:flex">
          <a href="#features" className="transition hover:text-violet-300">
            Features
          </a>
          <a href="#pricing" className="transition hover:text-violet-300">
            Pricing
          </a>
          <a href="#about" className="transition hover:text-violet-300">
            About
          </a>
          <a href="#faq" className="transition hover:text-violet-300">
            FAQ
          </a>
        </nav>

        <button
          onClick={onToggleMenu}
          className="mr-2 cursor-pointer rounded-lg border border-slate-700 px-3 py-2 text-xs transition hover:border-violet-400 md:hidden"
        >
          <span className="flex items-center gap-2">
            <FaBars />
            Menu
          </span>
        </button>

        <button className="hidden cursor-pointer rounded-lg border border-slate-700 px-5 py-2 text-sm font-medium transition hover:border-violet-400 hover:text-violet-300 md:inline-flex md:items-center md:gap-2">
          <FaEnvelope />
          Book a Demo
        </button>
      </header>

      {menuOpen && (
        <div className="fixed left-1/2 top-20 z-40 w-[min(95%,72rem)] -translate-x-1/2 rounded-2xl border border-slate-800 bg-slate-900/95 p-4 md:hidden">
          <div className="flex flex-col gap-3 text-sm text-slate-300">
            <a
              href="#features"
              onClick={onCloseMenu}
              className="transition hover:text-violet-300"
            >
              Features
            </a>
            <a
              href="#pricing"
              onClick={onCloseMenu}
              className="transition hover:text-violet-300"
            >
              Pricing
            </a>
            <a
              href="#about"
              onClick={onCloseMenu}
              className="transition hover:text-violet-300"
            >
              About
            </a>
            <a
              href="#faq"
              onClick={onCloseMenu}
              className="transition hover:text-violet-300"
            >
              FAQ
            </a>
            <button
              onClick={onCloseMenu}
              className="mt-2 inline-flex items-center justify-center gap-2 rounded-lg bg-violet-600 transition hover:bg-violet-500 px-4 py-2 font-semibold text-white"
            >
              <FaEnvelope />
              Book a Demo
            </button>
          </div>
        </div>
      )}
    </>
  );
}
