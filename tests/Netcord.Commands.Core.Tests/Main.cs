using Xunit;

namespace NeverToxic.Netcord.Commands.Core.Tests
{
    /// <summary>
    /// Main test.
    /// </summary>
    public class Main
    {
        /// <summary>
        /// Test.
        /// </summary>
        [Fact]
        public void Test()
        {
            Core.Main test = new();
            Assert.True(test.Test());
        }
    }
}
