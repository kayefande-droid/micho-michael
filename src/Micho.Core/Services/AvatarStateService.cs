using Micho.Core.Models;

namespace Micho.Core.Services;
public sealed class AvatarStateService
{
    public AvatarState CurrentState { get; private set; } = AvatarState.Idle;
    public event Action<AvatarState>? StateChanged;

    public void SetState(AvatarState state)
    {
        if (CurrentState == state) return;
        CurrentState = state;
        StateChanged?.Invoke(state);
    }

    public void Reset() { SetState(AvatarState.Idle); }
}