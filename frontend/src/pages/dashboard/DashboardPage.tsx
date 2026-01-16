import Header from '@/widgets/Header/Header'
import StatsCards from '@/widgets/StatsCards/StatsCards'
import ProgressTracker from '@/widgets/ProgressTracker/ProgressTracker'
import ActivityList from '@/widgets/ActivityList/ActivityList'
import RewardList from '@/widgets/RewardList/RewardList'

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-[#FBF7F2]">
      {/* Шапка сверху */}
      <Header />

      {/* Основной контент */}
      <main className="p-6 max-w-7xl mx-auto">
        <StatsCards />
        
        <div className="mt-6">
          <ProgressTracker />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
          <ActivityList />
          <RewardList />
        </div>
      </main>
    </div>
  )
}
