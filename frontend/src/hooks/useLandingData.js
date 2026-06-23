import { useEffect, useState } from "react";
import { getLandingData } from "../api/landingApi";
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

const iconMap = {
  SiZalo,
  FaCloud,
  FaMicrosoft,
  FaSlack,
  FaRegFileAlt,
  FaSalesforce,
  FaHubspot,
  FaAws,
  FaBolt,
  FaBrain,
  FaChartLine,
  FaLock,
  FaRobot,
};

export const useLandingData = () => {
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await getLandingData();

        const transformedData = {
          ...result,
          integrations: result.integrations?.map((item) => ({
            ...item,
            icon: iconMap[item.icon] || null,
          })),
          showcases: result.showcases?.map((item) => ({
            ...item,
            icon: iconMap[item.icon] || null,
          })),
          services: result.services?.map((item) => ({
            ...item,
            icon: iconMap[item.icon] || null,
          })),
          features: result.features?.map((item) => ({
            ...item,
            icon: iconMap[item.icon] || null,
          })),
        };

        setData(transformedData);
      } catch (error) {
        console.error(error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  return { data, isLoading };
};
