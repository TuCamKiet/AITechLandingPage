import {
  FaAws,
  FaBolt,
  FaBrain,
  FaChartLine,
  FaCloud,
  FaHubspot,
  FaLock,
  FaMicrosoft,
  FaRegFileAlt,
  FaRobot,
  FaSalesforce,
  FaSlack,
} from "react-icons/fa";
import { SiZalo } from "react-icons/si";

export const stats = [
  { label: "Active Students Taught", value: "250K+" },
  { label: "Average Score Improved", value: "34%" },
  { label: "Grading Hours Saved", value: "1.2M+" },
  { label: "Partner Schools", value: "120+" },
];

export const features = [
  {
    icon: FaBrain,
    title: "Personalized Learning Paths",
    description:
      "Dynamically adapt course materials, quizzes, and pacing to match each student's unique learning style and proficiency level.",
  },
  {
    icon: FaChartLine,
    title: "Real-Time Student Analytics",
    description:
      "Identify learning gaps instantly. Give educators a live dashboard of student progress, struggles, and breakthrough moments.",
  },
  {
    icon: FaLock,
    title: "FERPA-Compliant Security",
    description:
      "Keep student data strictly confidential with enterprise-grade encryption, role-based access, and academic compliance protocols.",
  },
];

export const services = [
  {
    icon: FaRobot,
    name: "24/7 AI Teaching Assistant",
    summary:
      "Provide students with instant, conversational tutoring on complex topics, available any time of day.",
  },
  {
    icon: FaBolt,
    name: "Grading & Feedback Copilot",
    summary:
      "Automate rubric-based grading for assignments and generate constructive, personalized feedback in seconds.",
  },
  {
    icon: FaChartLine,
    name: "Intervention Intelligence",
    summary:
      "Predict which students are at risk of falling behind before they fail a test, allowing for proactive intervention.",
  },
];

export const showcases = [
  {
    icon: FaCloud,
    title: "Educator Dashboard",
    description:
      "Monitor classroom engagement, assignment completion rates, and curriculum effectiveness in one unified view.",
    metric: "Save 12hrs/week",
  },
  {
    icon: FaRegFileAlt,
    title: "Dynamic Lesson Builder",
    description:
      "Turn a static syllabus into interactive modules, flashcards, and practice exams with a single click.",
    metric: "10x faster prep",
  },
  {
    icon: FaBrain,
    title: "Skill Mastery Engine",
    description:
      "Pinpoint the exact underlying concepts a student is missing and automatically generate targeted practice problems.",
    metric: "+40% retention",
  },
];

export const workflowSteps = [
  {
    step: "01",
    title: "Curriculum Ingestion",
    detail:
      "Upload your existing syllabus, textbooks, and past exams. Our AI securely learns your specific course material and teaching style.",
  },
  {
    step: "02",
    title: "Deploy Your Custom Tutor",
    detail:
      "Launch an AI teaching assistant directly to your students. It answers questions strictly based on your approved curriculum.",
  },
  {
    step: "03",
    title: "Learn, Adapt, & Improve",
    detail:
      "As students interact, the platform identifies common stumbling blocks and suggests curriculum improvements to the educator.",
  },
];

export const integrations = [
  { name: "Zalo", icon: SiZalo },
  { name: "Google Workspace", icon: FaCloud },
  { name: "Microsoft Teams", icon: FaMicrosoft },
  { name: "Slack", icon: FaSlack },
  { name: "Notion", icon: FaRegFileAlt },
  { name: "Salesforce (AITeach)", icon: FaSalesforce },
  { name: "HubSpot", icon: FaHubspot },
  { name: "AWS Cloud", icon: FaAws },
];

export const previews = [
  {
    quote:
      "The AI tutor helped our students grasp complex calculus concepts at 2 AM. Our class average went up by a full letter grade.",
    author: "Prof. Maya Rios",
    role: "Head of Mathematics, Lumina University",
  },
  {
    quote:
      "Grading 150 essays used to take my entire weekend. Now, the feedback copilot does the heavy lifting, and I just review.",
    author: "Oliver Grant",
    role: "Literature Teacher, Nova High School",
  },
  {
    quote:
      "Our online bootcamp completion rates skyrocketed after implementing the predictive learning paths. It's a massive competitive advantage.",
    author: "Sana Idris",
    role: "Director of Education, ApexCode",
  },
];

export const pricing = [
  {
    tier: "Educator",
    monthly: "$29",
    annual: "$24",
    description: "Perfect for individual teachers managing a few classrooms.",
    features: ["Up to 100 students", "AI Grading Assistant", "Basic analytics"],
  },
  {
    tier: "Department",
    monthly: "$149",
    annual: "$119",
    description: "For academic departments standardizing their tech stack.",
    features: [
      "Up to 1,000 students",
      "Custom Curriculum Ingestion",
      "Priority support",
    ],
    popular: true,
  },
  {
    tier: "Campus",
    monthly: "Custom",
    annual: "Custom",
    description: "Campus-wide deployment for schools and universities.",
    features: [
      "LMS Integration (Canvas/Blackboard)",
      "FERPA & SOC2 Compliance",
      "Dedicated Success Manager",
    ],
  },
];

export const faqs = [
  {
    q: "How long does it take the AI to learn my syllabus?",
    a: "Usually under 24 hours. Simply upload your PDFs, slide decks, and reading materials, and the AI models itself around your content.",
  },
  {
    q: "Is student data kept secure and private?",
    a: "Yes. We operate with strict FERPA guidelines. Student data is never used to train public models, and instances are completely siloed.",
  },
  {
    q: "Will the AI give students the answers to tests?",
    a: "No. You can configure the AI's 'guardrails' to act strictly as a Socratic tutor—guiding students to the answer without doing the work for them.",
  },
];

export const team = [
  { name: "Reza MK", role: "CEO & Former Educator" },
  { name: "Morteza P", role: "CTO & AITeach Architect" },
  { name: "Soheil MV", role: "Head of Curriculum Design" },
];
