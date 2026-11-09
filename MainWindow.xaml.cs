using System;
using System.Windows;
using System.Windows.Input;
using System.Windows.Media.Animation;
using System.Windows.Threading;

namespace MICHO;

/// <summary>
/// MainWindow for MICHO - Windows 11 Dynamic Island with AI Avatar
/// </summary>
public partial class MainWindow : Window
{
    private readonly DispatcherTimer _timer;
    private bool _isExpanded = false;

    public MainWindow()
    {
        InitializeComponent();

        // Initialize time display timer
        _timer = new DispatcherTimer
        {
            Interval = TimeSpan.FromSeconds(1)
        };
        _timer.Tick += Timer_Tick;
        _timer.Start();

        // Initialize state - collapsed by default
        ToggleState(false);

        // Drag detection - allow dragging from the glass background
        GlassBackground.MouseLeftButtonDown += (s, e) => DragMove();

        // Set initial focus
        Focus();
    }

    private void ToggleState(bool expand)
    {
        _isExpanded = expand;

        if (_isExpanded)
        {
            // Expand animation - show expanded panel, hide collapsed
            CollapsedPanel.Visibility = Visibility.Collapsed;
            ExpandedPanel.Visibility = Visibility.Visible;
        }
        else
        {
            // Collapse animation - show collapsed panel, hide expanded
            CollapsedPanel.Visibility = Visibility.Visible;
            ExpandedPanel.Visibility = Visibility.Collapsed;
        }
    }

    private void Timer_Tick(object? sender, EventArgs e)
    {
        // Update time display
        TimeTextBlock.Text = DateTime.Now.ToString("HH:mm:ss");
    }

    private void Border_MouseLeftButtonDown(object sender, MouseButtonEventArgs e)
    {
        // Toggle island state on click
        ToggleState(!_isExpanded);
        DragMove();
    }

    private void PauseButton_Click(object sender, RoutedEventArgs e)
    {
        // Pause playback
    }

    private void PlayButton_Click(object sender, RoutedEventArgs e)
    {
        // Play playback
    }

    private void StopButton_Click(object sender, RoutedEventArgs e)
    {
        // Stop playback
    }

    private void Window_Closed(object? sender, EventArgs e)
    {
        _timer?.Stop();
    }
}
