import { Pie } from 'react-chartjs-2';
import { Chart, ArcElement, Tooltip, Legend } from 'chart.js';

Chart.register(ArcElement, Tooltip, Legend);

const VehiclePieChart = ({ data }) => {
    // const vehicleData = Object.values(data)
  const distributionData = {
    labels: ['2 Wheeler', 'Car', 'Bus', 'Minibus', 'Tempo', 'Truck'],
    datasets: [
      {
        label: "Vehicle Count",
        data: [10, 20, 40, 13, 20, 14],
        backgroundColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(10, 6, 102, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(10, 6, 102, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
        ],
        borderWidth: 2,
      },
    ],
  };

  return (
    <Pie data={distributionData} />
  );
};

export default VehiclePieChart;
