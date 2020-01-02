package main

import (
	"reflect"
	"testing"
)

var testObjects = []Obj{
	{
		weight: 2,
		cpu:    2,
		mem:    2,
	},
	{
		weight: 3,
		cpu:    2,
		mem:    2,
	},
	{
		weight: 2,
		cpu:    2,
		mem:    2,
	},
	{
		weight: 2,
		cpu:    2,
		mem:    2,
	},
	{
		weight: 2,
		cpu:    2,
		mem:    2,
	},
	{
		weight: 2,
		cpu:    2,
		mem:    3,
	},
	{
		weight: 2,
		cpu:    3,
		mem:    2,
	},
}

func Test_cpu(t *testing.T) {
	type args struct {
		o []Obj
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Zero Objs",
			args: args{
				o: []Obj{},
			},
			want: 0,
		},
		{
			name: "Test first 2 Objs",
			args: args{
				o: testObjects[:2],
			},
			want: 4,
		},
		{
			name: "Test last 2 Objs",
			args: args{
				o: testObjects[5:],
			},
			want: 5,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Cpu(tt.args.o); got != tt.want {
				t.Errorf("cpu() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_heavier(t *testing.T) {
	type args struct {
		left  []Obj
		right []Obj
		m     func([]Obj) int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "left heavier",
			args: args{
				left:  testObjects[1:2],
				right: testObjects[0:1],
				m:     weight,
			},
			want: 1,
		},
		{
			name: "right heavier",
			args: args{
				left:  testObjects[0:1],
				right: testObjects[1:2],
				m:     weight,
			},
			want: 2,
		},
		{
			name: "equal heavy",
			args: args{
				left:  testObjects[0:1],
				right: testObjects[0:1],
				m:     weight,
			},
			want: 0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := heavier(tt.args.left, tt.args.right, tt.args.m); got != tt.want {
				t.Errorf("heavier() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_findOddItem(t *testing.T) {
	type args struct {
		o []Obj
		f func([]Obj) int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Find Mem!",
			args: args{
				o: testObjects,
				f: mem,
			},
			want: 6,
		},
		{
			name: "Find Weight!",
			args: args{
				o: testObjects,
				f: weight,
			},
			want: 3,
		},
		{
			name: "Find CPU!",
			args: args{
				o: testObjects,
				f: Cpu,
			},
			want: 7,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findOddItem(tt.args.o, tt.args.f); got != tt.want {
				t.Errorf("findOddItem() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_mem(t *testing.T) {
	type args struct {
		o []Obj
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Zero Objs",
			args: args{
				o: []Obj{},
			},
			want: 0,
		},
		{
			name: "Test first 2 Objs",
			args: args{
				o: testObjects[:2],
			},
			want: 4,
		},
		{
			name: "Test last 2 Objs",
			args: args{
				o: testObjects[5:],
			},
			want: 5,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := mem(tt.args.o); got != tt.want {
				t.Errorf("mem() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_heavierV2(t *testing.T) {
	type args struct {
		left  []Obj
		right []Obj
		m     func([]Obj) int
	}
	tests := []struct {
		name    string
		args    args
		want    []Obj
		wantErr bool
	}{
		{
			name: "group1 heavier",
			args: args{
				left:  testObjects[1:2],
				right: testObjects[0:1],
				m:     weight,
			},
			want: testObjects[1:2],
		},
		{
			name: "right heavier",
			args: args{
				left:  testObjects[0:1],
				right: testObjects[1:2],
				m:     weight,
			},
			want: testObjects[1:2],
		},
		{
			name: "equal heavy",
			args: args{
				left:  testObjects[0:1],
				right: testObjects[0:1],
				m:     weight,
			},
			want:    []Obj{},
			wantErr: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := heavierV2(tt.args.left, tt.args.right, tt.args.m)
			if (err != nil) != tt.wantErr {
				t.Errorf("heavierV2() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("heavierV2() = %v, want %v", got, tt.want)
			}
		})
	}
}
