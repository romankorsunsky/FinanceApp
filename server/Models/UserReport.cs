namespace b1.Models
{
    public class UserReport
    {
        public string UserId { get; set; }
        public List<AssetGain> PerAssetGain { get; set; } = null!;
        public double CurrentBalance { get; set; }
        public double TotalPortfoliosWorth { get; set; }
        public int OpenShortPositionsCount { get; set; }
        public int OpenLongPositionsCount { get; set; }

        public UserReport(string userId, double currentBalance, double totalPtfWorth, int openShortCount,
            int openLongCount, List<AssetGain> assetGains)
        {
            UserId = userId;
            CurrentBalance = currentBalance;
            TotalPortfoliosWorth = totalPtfWorth;
            OpenShortPositionsCount = openShortCount;
            OpenLongPositionsCount = openLongCount;
            PerAssetGain = assetGains;
        }
    }
    public struct AssetGain
    {
        public string AssetName { get; set; }
        public double Gain { get; set; }
        public AssetGain(string name, double gain)
        {
            AssetName = name;
            Gain = gain;
        }
    }
}