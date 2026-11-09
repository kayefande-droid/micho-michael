using Micho.Core.Models;

namespace Micho.Core.Services;
public sealed class IslandController
{
    public IslandState CurrentState { get; private set; } = IslandState.Compact;
    public event Action<IslandState>? StateChanged;

    public void SetState(IslandState state)
    {
        if (CurrentState == state) return;
        CurrentState = state;
        StateChanged?.Invoke(state);
    }

    public void Expand() { SetState(IslandState.Expanded); }
    public void Collapse() { SetState(IslandState.Compact); }
    public void ShowAssistant() { SetState(IslandState.Assistant); }
    public void ShowMusic() { SetState(IslandState.Music); }
}