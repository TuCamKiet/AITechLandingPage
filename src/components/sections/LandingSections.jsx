import { FaArrowLeft, FaArrowRight, FaCheckCircle } from "react-icons/fa";

export default function LandingSections({
  stats,
  workflowSteps,
  services,
  showcases,
  activeShowcase,
  setActiveShowcase,
  features,
  previews,
  activePreview,
  setActivePreview,
  integrations,
  pricing,
  annualBilling,
  setAnnualBilling,
  team,
  faqs,
  openFaq,
  setOpenFaq,
}) {
  return (
    <main className="space-y-24">
      <section
        data-reveal
        className="reveal-up grid gap-12 lg:grid-cols-2 lg:items-center"
      >
        <div>
          <p className="mb-4 inline-flex rounded-full border border-violet-400/30 bg-violet-400/10 px-4 py-1 text-sm text-violet-300 animate-pulse">
            Next-Generation AI for Educators & Institutions
          </p>
          <h1 className="mb-6 bg-linear-to-r from-white to-violet-200 bg-clip-text text-4xl font-bold leading-tight text-transparent sm:text-5xl">
            Empower your classroom with personalized AI teaching assistants.
          </h1>
          <p className="mb-8 max-w-xl text-lg text-slate-300">
            We help educators and institutions deploy secure, curriculum-aligned
            AI to automate grading, personalize learning, and boost student
            success.
          </p>
          <div className="flex flex-wrap gap-4 justify-center">
            <button className="rounded-lg bg-violet-600 px-6 py-3 font-semibold text-white shadow-lg shadow-violet-500/20 transition hover:-translate-y-0.5 hover:bg-violet-500">
              Try Educator Plan
            </button>
            <button className="rounded-lg border border-slate-600 px-6 py-3 font-semibold transition hover:border-violet-400 hover:text-violet-300">
              See Campus Demo
            </button>
          </div>

          <div className="mt-8 grid grid-cols-2 gap-4 sm:grid-cols-4">
            {stats.map((item) => (
              <div
                key={item.label}
                className="rounded-xl border border-slate-800 bg-slate-900/40 p-3 transition-all duration-300 hover:-translate-y-1 hover:border-violet-400/40"
              >
                <p className="text-xl font-bold text-violet-300">
                  {item.value}
                </p>
                <p className="text-xl text-slate-400">{item.label}</p>
              </div>
            ))}
          </div>
        </div>

        <div className="relative rounded-2xl border border-slate-800 bg-slate-900/60 p-6 shadow-2xl shadow-violet-500/10">
          <div className="absolute -inset-0.5 -z-10 rounded-2xl bg-linear-to-r from-violet-500/15 to-white/10 blur-md" />
          <div className="mb-6 flex items-center justify-between">
            <h2 className="text-lg font-semibold">Active Classroom AI</h2>
            <span className="rounded-full bg-teal-400/15 px-3 py-1 text-xs text-teal-300">
              +34% Avg. Score
            </span>
          </div>

          <div className="space-y-4">
            {["Automated Grading", "24/7 Tutoring", "Curriculum Ingestion"].map(
              (item) => (
                <div
                  key={item}
                  className="flex items-center justify-between rounded-xl border border-slate-800 bg-slate-950/70 px-4 py-3 transition-all duration-300 hover:border-violet-400/40 hover:bg-slate-900"
                >
                  <span className="text-slate-200">{item}</span>
                  <span className="text-sm text-violet-300">AI Active</span>
                </div>
              ),
            )}
          </div>
        </div>
      </section>

      <section data-reveal className="reveal-up">
        <div className="mb-6 flex flex-wrap items-center gap-3 text-xs uppercase tracking-widest text-slate-400">
          <span>Trusted by</span>
          {[
            "Lumina Univ",
            "ApexCode",
            "Nova High",
            "EduTech",
            "Pioneer Prep",
          ].map((brand) => (
            <span
              key={brand}
              className="rounded-full border border-slate-700 px-3 py-1"
            >
              {brand}
            </span>
          ))}
        </div>
      </section>

      <section
        data-reveal
        className="reveal-up rounded-2xl border border-slate-800 bg-slate-900/35 p-8"
      >
        <h2 className="mb-8 text-2xl font-semibold md:text-3xl">
          How We Launch Your Custom Tutor
        </h2>
        <div className="grid gap-6 md:grid-cols-3">
          {workflowSteps.map((item) => (
            <article
              key={item.step}
              className="rounded-xl border border-slate-800 bg-slate-900/50 p-6 transition-all duration-300 hover:-translate-y-1 hover:border-violet-400/40"
            >
              <p className="mb-3 text-sm font-semibold tracking-widest text-violet-300">
                {item.step}
              </p>
              <h3 className="mb-3 text-xl font-semibold">{item.title}</h3>
              <p className="text-slate-300">{item.detail}</p>
            </article>
          ))}
        </div>
      </section>

      <section id="features" data-reveal className="reveal-up">
        <h2 className="mb-8 text-2xl font-semibold md:text-3xl">
          AITeach Products & Services
        </h2>
        <div className="grid gap-6 md:grid-cols-3">
          {services.map((service) => (
            <article
              key={service.name}
              className="rounded-xl border border-slate-800 bg-slate-900/40 p-6 transition-all duration-300 hover:-translate-y-1.5 hover:border-violet-400 hover:shadow-lg hover:shadow-violet-500/10"
            >
              <service.icon className="mb-3 text-xl text-violet-300" />
              <h3 className="mb-3 text-xl font-semibold">{service.name}</h3>
              <p className="text-slate-300">{service.summary}</p>
            </article>
          ))}
        </div>
      </section>

      <section
        data-reveal
        className="reveal-up rounded-2xl border border-slate-800 bg-slate-900/40 p-8"
      >
        <div className="mb-6 flex items-center justify-between gap-3">
          <h2 className="text-2xl font-semibold md:text-3xl">
            Platform Preview Slider
          </h2>
          <div className="flex gap-2">
            <button
              onClick={() =>
                setActiveShowcase(
                  (prev) => (prev - 1 + showcases.length) % showcases.length,
                )
              }
              className="inline-flex h-9 w-9 items-center justify-center rounded-md border border-slate-700 text-sm transition hover:border-violet-400"
              aria-label="Previous slide"
            >
              <FaArrowLeft />
            </button>
            <button
              onClick={() =>
                setActiveShowcase((prev) => (prev + 1) % showcases.length)
              }
              className="inline-flex h-9 w-9 items-center justify-center rounded-md border border-slate-700 text-sm transition hover:border-violet-400"
              aria-label="Next slide"
            >
              <FaArrowRight />
            </button>
          </div>
        </div>

        <div className="overflow-hidden rounded-xl border border-slate-800">
          <div
            className="flex transition-transform duration-700 ease-out"
            style={{ transform: `translateX(-${activeShowcase * 100}%)` }}
          >
            {showcases.map((item) => (
              <article
                key={item.title}
                className="min-w-full bg-linear-to-br from-slate-900 to-slate-950 p-8"
              >
                <p className="mb-3 inline-flex rounded-full border border-violet-400/30 bg-violet-400/10 px-3 py-1 text-xs text-violet-300">
                  {item.metric}
                </p>
                <item.icon className="mb-4 text-2xl text-violet-300" />
                <h3 className="mb-3 text-2xl font-semibold text-violet-200">
                  {item.title}
                </h3>
                <p className="max-w-2xl text-slate-300">{item.description}</p>
              </article>
            ))}
          </div>
        </div>

        <div className="mt-4 flex justify-center gap-2">
          {showcases.map((item, index) => (
            <button
              key={item.title}
              onClick={() => setActiveShowcase(index)}
              className={`h-2.5 rounded-full transition-all ${activeShowcase === index ? "w-8 bg-violet-400" : "w-2.5 bg-slate-600"}`}
            />
          ))}
        </div>
      </section>

      <section data-reveal className="reveal-up">
        <h2 className="mb-8 text-2xl font-semibold md:text-3xl">
          Why Educators Choose Us
        </h2>
        <div className="grid gap-6 md:grid-cols-3">
          {features.map((feature) => (
            <article
              key={feature.title}
              className="rounded-xl border border-slate-800 bg-slate-900/40 p-6 transition-all duration-300 hover:-translate-y-1.5 hover:border-violet-400 hover:shadow-lg hover:shadow-violet-500/10"
            >
              <feature.icon className="mb-3 text-xl text-violet-300" />
              <h3 className="mb-3 text-xl font-semibold">{feature.title}</h3>
              <p className="text-slate-300">{feature.description}</p>
            </article>
          ))}
        </div>
      </section>

      <section
        data-reveal
        className="reveal-up rounded-2xl border border-slate-800 bg-slate-900/40 p-8"
      >
        <div className="mb-6 flex items-center justify-between gap-3">
          <h2 className="text-2xl font-semibold md:text-3xl">
            What Teachers & Admins Say
          </h2>
          <div className="flex gap-2">
            <button
              onClick={() =>
                setActivePreview(
                  (prev) => (prev - 1 + previews.length) % previews.length,
                )
              }
              className="inline-flex h-9 w-9 items-center justify-center rounded-md border border-slate-700 text-sm transition hover:border-violet-400"
              aria-label="Previous preview"
            >
              <FaArrowLeft />
            </button>
            <button
              onClick={() =>
                setActivePreview((prev) => (prev + 1) % previews.length)
              }
              className="inline-flex h-9 w-9 items-center justify-center rounded-md border border-slate-700 text-sm transition hover:border-violet-400"
              aria-label="Next preview"
            >
              <FaArrowRight />
            </button>
          </div>
        </div>

        <div className="overflow-hidden">
          <div
            className="flex transition-transform duration-700 ease-out"
            style={{ transform: `translateX(-${activePreview * 100}%)` }}
          >
            {previews.map((item) => (
              <article
                key={item.author}
                className="min-w-full rounded-xl border border-slate-800 bg-slate-950/50 p-8"
              >
                <p className="mb-6 text-xl leading-relaxed text-slate-200">
                  "{item.quote}"
                </p>
                <p className="font-medium text-violet-300">{item.author}</p>
                <p className="text-sm text-slate-400">{item.role}</p>
              </article>
            ))}
          </div>
        </div>

        <div className="mt-4 flex justify-center gap-2">
          {previews.map((item, index) => (
            <button
              key={item.author}
              onClick={() => setActivePreview(index)}
              className={`h-2.5 rounded-full transition-all ${activePreview === index ? "w-8 bg-violet-400" : "w-2.5 bg-slate-600"}`}
            />
          ))}
        </div>
      </section>

      <section
        data-reveal
        className="reveal-up rounded-2xl border border-slate-800 bg-slate-900/35 p-8"
      >
        <h2 className="mb-8 text-2xl font-semibold md:text-3xl">
          Built to Integrate with Your Tools
        </h2>
        <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4">
          {integrations.map((item) => (
            <div
              key={item.name}
              className="rounded-lg border border-slate-800 bg-slate-950/50 px-4 py-3 text-center text-sm font-medium text-slate-200 transition-all duration-300 hover:-translate-y-1.5 hover:border-violet-400 hover:shadow-lg hover:shadow-violet-400/40"
            >
              <item.icon className="mx-auto mb-2 text-base text-violet-300" />
              {item.name}
            </div>
          ))}
        </div>
      </section>

      <section
        id="pricing"
        data-reveal
        className="reveal-up rounded-2xl border border-slate-800 bg-slate-900/30 p-8"
      >
        <div className="mb-8 flex flex-wrap items-center justify-center gap-4 md:justify-between">
          <h2 className="w-full text-center text-2xl font-semibold md:w-auto md:text-left md:text-3xl">
            Simple Pricing For Every Stage
          </h2>
          <div className="mx-auto rounded-lg border border-slate-700 p-1 text-sm md:mx-0">
            <button
              onClick={() => setAnnualBilling(false)}
              className={`rounded-md px-4 py-2 transition-all duration-300 ${annualBilling ? "text-slate-400" : "bg-slate-100 text-slate-900"}`}
            >
              Monthly
            </button>
            <button
              onClick={() => setAnnualBilling(true)}
              className={`rounded-md px-4 py-2 transition-all duration-300 ${annualBilling ? "bg-slate-600 text-white" : "text-slate-400"}`}
            >
              Annual
            </button>
          </div>
        </div>

        <div className="grid gap-6 md:grid-cols-3">
          {pricing.map((plan) => (
            <article
              key={plan.tier}
              className={`rounded-xl border p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-xl ${plan.popular ? "border-violet-400 bg-violet-400/10 shadow-lg shadow-violet-500/20" : "border-slate-800 bg-slate-950/50 hover:border-violet-400/40 hover:shadow-violet-500/10"}`}
            >
              <p className="mb-2 text-sm text-slate-400">{plan.tier}</p>
              <p className="mb-3 text-3xl font-bold transition-all duration-300">
                {annualBilling ? plan.annual : plan.monthly}
                {plan.monthly !== "Custom" && (
                  <span className="text-sm text-slate-400">/mo</span>
                )}
              </p>
              <p className="mb-4 text-slate-300">{plan.description}</p>
              <ul className="mb-6 space-y-2 text-sm text-slate-300">
                {plan.features.map((item) => (
                  <li key={item} className="flex items-center gap-2">
                    <FaCheckCircle className="mt-0.5 text-violet-300" />
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
              <button className="w-full rounded-lg border border-slate-600 px-4 py-2 font-medium transition hover:border-violet-400 hover:text-violet-300">
                Get Started
              </button>
            </article>
          ))}
        </div>
      </section>

      <section
        id="about"
        data-reveal
        className="reveal-up grid gap-8 rounded-2xl border border-slate-800 bg-linear-to-r from-slate-900 to-slate-900/40 p-8 md:grid-cols-2"
      >
        <div>
          <h2 className="mb-4 text-2xl font-semibold md:text-3xl">
            Built by Former Educators, For the Modern Classroom
          </h2>
          <p className="text-slate-300">
            We are a dedicated team of former educators, AITeach architects, and
            AI researchers focused on making personalized learning accessible to
            every student.
          </p>
        </div>

        <div className="space-y-4">
          {team.map((member) => (
            <div
              key={member.name}
              className="rounded-lg border border-slate-700 bg-slate-950/50 px-4 py-3 transition-all duration-300 hover:-translate-y-0.5 hover:border-violet-400/40"
            >
              <p className="font-medium">{member.name}</p>
              <p className="text-sm text-slate-400">{member.role}</p>
            </div>
          ))}
        </div>
      </section>

      <section
        id="faq"
        data-reveal
        className="reveal-up rounded-2xl border border-slate-800 bg-slate-900/40 p-8"
      >
        <h2 className="mb-6 text-2xl font-semibold md:text-3xl">
          Frequently Asked Questions
        </h2>
        <div className="space-y-3">
          {faqs.map((item, index) => {
            const isOpen = openFaq === index;
            return (
              <div
                key={item.q}
                className="rounded-lg border border-slate-700 bg-slate-950/40 transition-colors duration-300 hover:border-violet-400/40"
              >
                <button
                  onClick={() => setOpenFaq(isOpen ? -1 : index)}
                  className="flex w-full items-center justify-between px-4 py-3 text-left transition-colors duration-300 hover:text-violet-200"
                >
                  <span className="font-medium">{item.q}</span>
                  <span
                    className={`text-violet-400 transition-transform duration-300 ${isOpen ? "rotate-180" : ""}`}
                  >
                    +
                  </span>
                </button>
                <div
                  className={`faq-content px-4 text-slate-300 ${isOpen ? "faq-open pb-4" : ""}`}
                >
                  <p>{item.a}</p>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      <section
        data-reveal
        className="reveal-up rounded-2xl border border-violet-400/30 bg-violet-500/10 p-8 text-center"
      >
        <h2 className="mb-4 text-2xl font-semibold md:text-3xl">
          Ready to Transform Your Classroom?
        </h2>
        <p className="mx-auto mb-6 max-w-2xl text-slate-200">
          Launch your custom AI teaching assistant in under 24 hours. Join
          educators using our platform to save time and boost student retention.
        </p>
        <button className="rounded-lg bg-violet-600 px-7 py-3 font-semibold text-white shadow-lg shadow-violet-500/15 transition-all duration-300 hover:-translate-y-0.5 hover:bg-violet-500">
          Schedule Your AITeach Demo
        </button>
      </section>
    </main>
  );
}
