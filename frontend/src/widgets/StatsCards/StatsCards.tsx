export default function StatsCards() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <Card title="Total Units" value="47" />
      <Card title="Bonus Points" value="235" />
      <Card title="Free Rewards" value="3" />
    </div>
  )
}

function Card({ title, value }: any) {
  return (
    <div className="bg-white rounded-2xl p-6">
      <p className="text-sm text-gray-500">{title}</p>
      <p className="text-3xl font-bold">{value}</p>
    </div>
  )
}
