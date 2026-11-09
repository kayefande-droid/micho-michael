using Micho.Core.Models;

namespace Micho.Core.Services;
public sealed class DesktopEventBus
{
    public event Action<object>? ActivityReceived;

    public void Publish<T>(T activity) where T : notnull
    {
        ActivityReceived?.Invoke(activity);
    }
}